import talib as ta;
import AnalyzeTools.AnalyzeTools as ind


class MACD(ind.AnalyzeTool):
    #__close = None
    __diff = None
    __dea = None
    __up2u = None
    __fastperiod = 12
    __slowperiod = 26
    __signalperiod = 9

    def __init__(self,sourceData):
        #ind.AnalyzeTool.__init__(sourceData)
        super(MACD, self).__init__(sourceData)

    def calculate(self):
        self.__diff,self.__dea,self.__up2u = ta.MACD(self._sourceData,
                                                     fastperiod=self.__fastperiod,
                                                     slowperiod=self.__slowperiod,
                                                     signalperiod=self.__signalperiod)

    def getDiff(self):
        return self.__diff

    def getDea(self):
        return self.__dea;

    def getUp2u(self):
        return self.__up2u;
    def setFastPeriod(self,fastperiod):
        self.__fastperiod = fastperiod

    def setSlowPeriod(self,slowperiod):
        self.__slowperiod = slowperiod

    def setSignalPeriod(self,signalperiod):
        self.__signalperiod = signalperiod
