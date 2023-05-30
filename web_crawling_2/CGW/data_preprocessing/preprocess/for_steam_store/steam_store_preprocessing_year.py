# 5개년에 대한 steam store data 전처리 코드 

import pandas as pd
import numpy as np
import json
from datetime import datetime
import re

years = [2018,2019,2020,2021,2022]
for year in years:

    file_path = f"C:\Users\NT550-052\OneDrive\바탕 화면\ASAC\프로젝트\ML\web_crawling\CGW\data_preprocessing\mid_data\jsonfiles\steam_store_data_{year}.json"

    with open(file_path, 'r',encoding="cp949") as f:
        data = json.load(f)

    steam_df = pd.DataFrame(columns=["appid","required_age","is_free","controller_support","dlc","metacritic","windows","mac","linux","platforms_num","recommendations","achievements","release_date"])

    for idx,item in enumerate(data.items()):
        key = item[0]
        value = item[1]
        row = [key]

        for k, v in value.items():
            if k == "platforms":
                if type(v) == dict:
                    for pk in v.keys():
                        row.append(int(v[pk]))
                    row.append(sum(v.values()))
                else:
                    for _ in range(4):
                        row.append(np.nan)

            else:
                row.append(v)
        
        steam_df.loc[idx] = row

    save_path = f"C:\Users\NT550-052\OneDrive\바탕 화면\ASAC\프로젝트\ML\web_crawling\CGW\data_preprocessing\mid_data\csvs\steam_store_df_{year}.csv"

    steam_df.to_csv(save_path,sep=";")