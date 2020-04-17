import analyzetools.AnalyzeTools as ind

import talib as ta


class MA(ind.AnalyzeTool):
    __timeperiod = 5

    def __init__(self,sourceData):
        #ind.AnalyzeTool.__init__(sourceData)
        super(MA, self).__init__(sourceData)

    def setTimeperiod(self,timeperiod):
        self.__timeperiod = timeperiod

    def calculate(self):
        self._result = ta.MA(self._sourceData,timeperiod=self.__timeperiod)
