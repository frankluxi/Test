#import pandas as pd
#import numpy as np
import talib as ta
import tushare as ts
#from matplotlib import rc
#rc('mathtext', default='regular')
#import seaborn as sns
#sns.set_style('white')
#%matplotlib inline

dw = ts.get_k_data("002142")
close = dw.close.values
dw['diff'], dw['dea'], dw['macdhist'] = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

dw[['close','diff','dea','macdhist']].plot()
dw['max'] = ta.MAX(close, timeperiod=20)
dw[['close','max']].plot();
print(dw)
diff, dea, macdhist = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
print(type(diff))