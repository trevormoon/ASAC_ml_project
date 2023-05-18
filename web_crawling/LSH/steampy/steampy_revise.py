from warnings import filterwarnings
filterwarnings('ignore')

from glob import glob
from tqdm import tqdm
from collections import deque

import requests
import multiprocessing
import pandas as pd
import numpy as np
import os

def extract(appid):
    flag = ''
    cwd = os.getcwd()
    check_path = glob(f'{cwd}\\**\\extract_doc\\steamspy.txt',recursive=True)[0]
    check_list = [i.replace('\n','') for i in open(check_path).readlines()]
    
    result_dict = {appid : { i : '' for i  in check_list } }
    res = requests.get(f'https://steamspy.com/api.php?request=appdetails&appid={appid}')
    
    if res.status_code != 200:
        flag = False
        return result_dict, flag
    
    res_json = res.json()
    
    for check in check_list:
        try:
            result_dict[appid][check] = res_json[check]
        except:
            continue
    flag = True
    
    return result_dict, flag

def run():
    
    cwd = os.getcwd()
    appid_dirs = glob(f'{cwd}\\**\\appid_list\\*.txt',recursive=True)
    check_path = glob(f'{cwd}\\**\\extract_doc\\steamspy.txt',recursive=True)[0]
    steamspy_dir = glob(f'{cwd}\\**\\steampy',recursive=True)[0]
    
    check_list = [i.replace('\n','') for i in open(check_path).readlines()]
    
    for appid_dir in appid_dirs:
        base_name = os.path.basename(appid_dir)
        if '2019' in base_name or '2018' in base_name:
            continue
        
        app_list = [i.replace('\n', '') for i in open(appid_dir).readlines()]

        result_last = {i : deque([]) for i in check_list}
        result_last["appid"] = app_list
        
        result_mid = {}
        result_error = {}
        with multiprocessing.Pool() as p:
            for val, flag in tqdm(p.imap_unordered(extract, app_list, 16), total = len(app_list)):
                result_mid.update(val)
                if flag == False:
                    result_error.update(val)
        
        for app in app_list:
            for check in check_list:
                result_last[check].append(result_mid[app][check])
        
        df = pd.DataFrame(result_last)
        
        df['price'] = df['price'].fillna(0)
        df['price'] = df['price'].astype(int) / 100
        
        df['initialprice'] = df['initialprice'].fillna(0)
        df['initialprice'] = df['initialprice'].astype(int) / 100
        
        df['num_lang'] = df['languages'].fillna('').apply(lambda x : len(x.split()))
        
        file_name = os.path.splitext(base_name)[0]
        
        df.to_csv(f'{steamspy_dir}\\{file_name}.csv', index=False, sep='\t')
    
if __name__ == '__main__':
    run()