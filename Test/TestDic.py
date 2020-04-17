import analyzetools.MACD as macd
import analyzetools.MA as ma

dic = {"MACD":macd.MACD,"MA":ma.MA}
ind = dic["MA"]
ind.getResult()