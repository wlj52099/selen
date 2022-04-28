import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\py\ce\1.csv',encoding='utf-8',index_col='number')


df=df.replace(r'^\s*$',np.nan,regex=True)
# df = df.where(df.notnull(), '')#处理nan
print(df)