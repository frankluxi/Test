from index.index import Index
import talib as ta
class MA(Index):
    __timeperiod = 5


    def __init__(self,sourceData):
        Index.__init__(sourceData)

    def setTimeperiod(self,timeperiod):
        self.__timeperiod = timeperiod

    def calculate(self):
        ta.MA(self._sourceData,timeperiod=self.__timeperiod)
