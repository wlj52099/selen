import time

import pandas as pd
from concurrent.futures import ThreadPoolExecutor,as_completed
import os
import random
def name(url):

    df = pd.read_csv(url,encoding='gbk')
    # del df['1']
    # print(df)
    # df.drop('Unnamed: 0', axis=1, inplace=True)  # 改变原始数据
    # df.to_csv(url)
    time.sleep(random.randint(1,3))
if __name__ == '__main__':
    dir = []
    file_dir = r'D:\py\ce'
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            f = file_dir+'\\'+file
            dir.append(f)
    print(dir)
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(name,url) for url in dir]
        for future in futures:
            print(future.result())
        # for future in as_completed(futures):
        #     print(future.result())
