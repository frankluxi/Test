import talib as ta
import numpy as np

p = np.array([1.0, 321.0, 231.0, 321.0, 45.0, 46.0, 57.0, 897.0, 987.0, 64.0, 78987.0, 31.0, 32.0, 654.0, 5.0])
s = ta.MA(p, 5)

print(s)