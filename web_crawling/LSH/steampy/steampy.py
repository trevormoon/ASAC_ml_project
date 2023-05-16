import requests
import multiprocessing
import pandas as pd
import numpy as np
from tqdm import tqdm
from collections import deque

def extract(appid):
    flag = ''
    
    check_list = [i.replace('\n','') for i in open(r'C:\Users\NT550-045\Desktop\ml2\ASAC_ml_project\web_crawling\LSH\extract_doc\steamspy.txt').readlines()]
    
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
    app_list = [i.replace('\n', '') for i in open(r'C:\Users\NT550-045\Desktop\ml2\ASAC_ml_project\web_crawling\LSH\appid_list\appid_2022.txt').readlines()]

    check_list = [i.replace('\n','') for i in open(r'C:\Users\NT550-045\Desktop\ml2\ASAC_ml_project\web_crawling\LSH\extract_doc\steamspy.txt').readlines()]

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
    
    df['price'] = df['price'].fillna(0, inplace=True)
    df['price'] = df['price'].astype(int) / 100
    
    df['initialprice'] = df['initialprice'].fillna(0, inplace=True)
    df['initialprice'] = df['initialprice'].astype(int) / 100
    
    df['num_lang'] = df['languages'].fillna('').apply(lambda x : len(x.split()))
    
    df.to_csv(r'C:\Users\NT550-045\Desktop\ml2\ASAC_ml_project\web_crawling\LSH\steampy\2022_steam_sept.csv', index=False, sep='\t')
    
if __name__ == '__main__':
    run()