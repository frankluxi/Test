import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Hello, Pandas")
s =pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range('20200101',periods=7)
print(dates)


print("--"*16 + "  DataFrame")

tmp1 = list('ABCD')
print(tmp1)

#df = pd.DataFrame(np.random.randn(7,4), AnalyzeTools=dates, columns=list('ABCD'))
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=tmp1)
# print(df)
print(df['A'])

print("------"*10+"按索引筛选")
print(df['20200101':'20200101'])
print("------"*10 + "loc +筛选值")
print(df.loc['20200101'])
print("------"*10 + "标签选择多轴")
print(df.loc['20200107',['C','D']])






print("--"*16)

#tmp = pd.DataFrame({'A': 1.4,
#                    'B': pd.Timestamp('20170102'),
#                   'C': pd.Series(1,AnalyzeTools=list(range(4)),dtype='float32'),
#                   'D': np.array([3] * 4,dtype='int32'),
#                   'E': pd.Categorical(["test","train","test","train"]),
#                   'F': 'foo'})
#print(tmp)







