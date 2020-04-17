from analyzetools.AnalyzeTools import AnalyzeTool
import talib as ta


class MAX(AnalyzeTool):
    __timeperiod = 5

    def __init__(self,sourceData):
        super(MAX, self).__init__(sourceData)

    def calculate(self):
        self._result = ta.MAX(self._sourceData,self.__timeperiod)

    def setTimeperiod(self, timeperiod):
        self.__timeperiod = timeperiod
