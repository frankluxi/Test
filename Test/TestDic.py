import AnalyzeTools.MACD as macd
import AnalyzeTools.MA as ma

dic = {"MACD":macd.MACD,"MA":ma.MA}
ind = dic["MA"]
ind.getResult()