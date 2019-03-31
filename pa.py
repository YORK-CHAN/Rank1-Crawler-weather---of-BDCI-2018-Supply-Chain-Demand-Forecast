# -*- coding: utf-8 -*-
#用来划分训练集和验证集
import pandas as pd
import lightgbm as lgb
import gc
import time
import operator
import xgboost as xgb
import numpy as np
from sklearn import preprocessing
from dateutil.parser import parse
from pandas import Series,DataFrame
import time
import datetime

import requests
r = requests.get('https://api.weather.com/v1/geocode/42.09999847/-70.66999817/observations/historical.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&startDate=20180911&endDate=20180911&units=m')
# print(r.json()['observations'][0].keys())



keys = list(r.json()['observations'][0].keys())
print(keys)
day = 20171101
result = []
while day<20180701:
    print(day)
    url = 'https://api.weather.com/v1/geocode/42.09999847/-70.66999817/observations/historical.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&startDate='+str(day)+'&endDate='+str(day)+'&units=m'
    response = requests.get(url)
    print(response.json())
    try:
        for item in response.json()['observations']:
            result.append(list(item.values()))
        day = int((datetime.datetime(int(str(day)[0:4]), int(str(day)[4:6]),int(str(day)[6:8])) + datetime.timedelta(days=1)).strftime("%Y%m%d"))
    except:
        print('%s出错 再次请求...'%day)
        pass
    time.sleep(2)
result = pd.DataFrame(result,columns=keys)
result.to_csv('arabia_weather_20171101-20180701.csv', index=None)

















