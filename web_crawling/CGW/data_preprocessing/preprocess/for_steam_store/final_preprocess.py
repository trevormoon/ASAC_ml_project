import pandas as pd
import numpy as np
from datetime import datetime
import re

years = [2018,2019,2020,2021,2022]
for year in years:
    path = f"C:\Users\NT550-052\OneDrive\바탕 화면\ASAC\프로젝트\ML\web_crawling\CGW\data_preprocessing\mid_data\csvs\steam_store_df_{year}.csv"
    
    data = pd.read_csv(path,sep=";")
    data.drop(columns="Unnamed: 0",inplace=True)
    
    # 메타크리틱,컨트롤러 0/1컬럼 만들기
    data["metacritic_tf"] = data["metacritic"].notnull().astype("int")
    data["controller_support"] = data["controller_support"].notnull().astype("int")
    
    # 기존 release_date drop
    data.drop(columns=["release_date","release_date_final"],inplace=True)
    
    # release_date 합치기
    date_path = f"C:\\Users\\NT550-052\\OneDrive\\바탕 화면\\ASAC\\프로젝트\\ML\\web_crawling\\CGW\\csvs\\{year}_date.csv"
    date = pd.read_csv(date_path)

    data = pd.merge(data,date,how="left",on="appid")
    data['new_date'] = pd.to_datetime(data["new_date"], format='%Y-%m-%d')
    
    today = "2023-05-19"
    today = datetime.strptime(today,'%Y-%m-%d')
    data["days_after_release"] = data["new_date"].apply(lambda x: (today - x).days)
    
    # 장르 범주 나누기
    # nan -> 0, 17,18,19 -> 18, 14,15,16 -> 15, 나머지 12
    
    data["required_age"].fillna(0,inplace=True)
    data["required_age"] = data["required_age"].astype("str")
    
    for idx,elem in enumerate(data["required_age"]):
        if "+" in elem:
            data["required_age"][idx] = elem.replace("+","")
        elif elem == "ALL":
            data["required_age"][idx] = "0"
    
    data["required_age"] = data["required_age"].astype("float")
    for idx,elem in enumerate(data["required_age"]):
        if elem > 16:
            data["required_age"][idx] = 18
        elif elem > 13:
            data["required_age"][idx] = 15
        elif elem > 0:
            data["required_age"][idx] = 12
            
    # 추천수 nan, 도전과제 nan, dlc nan을 0으로 
    data["recommendations"].fillna(0,inplace=True)
    data["achievements"].fillna(0,inplace=True)
    data["dlc"].fillna(0,inplace=True)
    
    # new_date rename
    data.rename(columns={"new_date":"release_date"},inplace=True)
    
    # 컬럼 순서 조정
    data = data[["appid","required_age","is_free","controller_support","dlc","metacritic","metacritic_tf","windows","mac","linux","platforms_num","recommendations","achievements","release_date","days_after_release"]]
    
    save_path = f"C:\Users\NT550-052\OneDrive\바탕 화면\ASAC\프로젝트\ML\web_crawling\CGW\data_preprocessing\mid_data\final\steam_store_after_pcs_{year}.csv"
    data.to_csv(save_path,sep=";")