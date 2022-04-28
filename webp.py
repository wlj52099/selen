import random
import time
import json
from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor

import requests
import threading
import pandas as pd
dict = {}
data = pd.read_csv(r'\\192.168.0.13\d\Landry\data.csv')
def re(d):
    resp = requests.get('https://api.mingdao.com/workflow/hooks/NjI2MTBiNWJjZTE0ODA0MmYwYjUzN2I0',data=d)
    print(resp.text)
    time.sleep(random.randint(0.5,1))
data = pd.read_csv(r'\\192.168.0.13\d\Landry\data.csv')
lable = list(data.columns.values)[0:len(list(data.columns.values))-1]
lisdic = []
for i in data.index:
    for l in lable:
        dict[l] = str(data[l].at[i])
    lisdic.append(dict)
    dict = {}
with ThreadPoolExecutor(max_workers=10) as pool:
    for url in lisdic:
        futures = pool.map(re,url)
        for req in futures:
            print(req)
    # for future in futures:
    #     print(future.result())
    # for future in as_completed(futures):
    #     print(future.result())无法使用
