import talib as ta
import numpy as np
import tushare as ts
import pandas as pd

p = np.array([1.0, 321.0, 231.0, 321.0, 45.0, 46.0, 57.0, 897.0, 987.0, 64.0, 78987.0, 31.0, 32.0, 654.0, 5.0])
s = ta.MAX(p, 6)

print(s)
print("finish")

# df = ts.get_realtime_quotes('002142')
# print(df.columns)
# # df.loc[0,'date','price','high', 'low']
#
#
# print(df.loc[0:,['date','price','high', 'low']])