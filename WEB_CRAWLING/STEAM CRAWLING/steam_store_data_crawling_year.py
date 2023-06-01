# 연도별로 따로 지정해주지 않고 한 파일로 여러 연도의 데이터를 수집 및 저장
# appid 불러오는 path는 지정요망 


from bs4 import BeautifulSoup
import requests
from collections import deque
import time
import numpy as np
import json

Z = ["required_age","is_free","controller_support","dlc","metacritic","platforms","recommendations","achievements","release_date"]

def please(id,idx,res):
    g_info = {}
    try:
        data = res.json()
        if data[str(id)]["success"] == True: # success == true
            keys = data[str(id)]["data"].keys()
            main = data[str(id)]["data"]
            
            for elem in Z:
                if elem in keys:
                    if elem in ["recommendations","achievements"]:
                        g_info[elem] = main[elem]["total"]
                    elif elem == "release_date":
                        g_info[elem] = main[elem]["date"]
                    elif elem == "metacritic":
                        g_info[elem] = main[elem]["score"]
                    elif elem == "dlc":
                        g_info[elem] = len(main[elem])
                    else:
                        g_info[elem] = main[elem]
                else:
                    g_info[elem] = np.nan
            print(idx,id,g_info)
        else: # success == false
            for elem in Z:
                g_info[elem] = np.nan
            print("error",idx,id,g_info)
                
    except: # 빈 페이지 load되는 데이터 
        for elem in Z:
            g_info[elem] = np.nan
        print("error",idx,id,g_info)
            
    finally:
        final_data[str(id)] = g_info

for year in [2019,2018]:
    file_path = f"C:/Users/NT550-052/OneDrive/바탕 화면/ASAC/프로젝트/ML/web_crawling/LSH/appid_list/appid_{year}.txt"
    file = open(file_path,"r")
    final_data = {}

    appids = []
    while True:
        line = file.readline()
        if not line: break
        appids.append(int(line.strip()))
    
    for idx,id in enumerate(appids):
        path = f"https://store.steampowered.com/api/appdetails?appids={id}"

        res = requests.get(path)
        if res.status_code == 200:
            please(id,idx,res)
        else:
            time.sleep(60)
            please(id,idx,res)
        time.sleep(1.5)
    print(final_data)

    save_path = f"C:/Users/NT550-052/OneDrive/바탕 화면/ASAC/프로젝트/ML 프로젝트/steam_store_data_{year}.json"
    with open(save_path,'w') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)