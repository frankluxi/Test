from abc import ABCMeta, ABC, abstractmethod
import pandas as pd

from AnalyzeTools.MA import MA
from AnalyzeTools.MACD import MACD
from AnalyzeTools.MAX import MAX
from Stock.KLineInterface import KLineInterface


class AbstractKline(KLineInterface, ABC):
    # 抽象类
    __metaclass__ = ABCMeta

    # K线数据，类型为DataFrame
    _KLineData = pd.DataFrame()

    # 分析工具MACD MAX，，，，，，
    _analyzeTools = {}

    def __init__(self):
        self._analyzeTools.update({'MA': MA(None)})
        self._analyzeTools.update({'MACD': MACD(None)})
        self._analyzeTools.update({'MAX': MAX(None)})

    def getData(self):
        return self._KLineData

    def _calculateMA(self, period):
        col = 'MA' + str(period);
        maTool = self._analyzeTools["MA"]
        maTool.setTimeperiod(period)
        maTool.setSourceData(self._KLineData.close.values)
        maTool.calculate()
        self._KLineData[col] = maTool.getResult()

    def _calculateMAX20(self):
        self.__calculateMAX(20)

    def _calculateMAX(self, period):
        col = 'MAX' + str(period);
        maxTool = self._analyzeTools["MAX"]
        maxTool.setTimeperiod(period)
        maxTool.setSourceData(self._KLineData.close.values)
        maxTool.calculate()
        self._KLineData[col] = maxTool.getResult()

    def _calculateMA5(self):
        self._calculateMA(5)

    # 10日均线
    def _calculateMA10(self):
        self._calculateMA(10)

    # 20日均线
    def _calculateMA20(self):
        self._calculateMA(20)

    # 30日均线
    def _calculateMA30(self):
        self._calculateMA(30)

    # 60日均线
    def _calculateMA60(self):
        self._calculateMA(60)

    # 120日均线
    def _calculateMA120(self):
        self._calculateMA(120)

    # 250日均线
    def _calculateMA250(self):
        self._calculateMA(250)

    def _calculateMACD(self, fastperiod=12, slowperiod=26, signalperiod=9):
        macdTool = self._analyzeTools["MACD"]
        macdTool.setFastPeriod(fastperiod)
        macdTool.setSlowPeriod(slowperiod)
        macdTool.setSignalPeriod(signalperiod)
        macdTool.setSourceData(self._KLineData.close.values)
        macdTool.calculate()
        self._KLineData['DIF'] = macdTool.getDiff()
        self._KLineData['DEA'] = macdTool.getDea();

    def _calculateMA(self, period):
        col = 'MA' + str(period)
        maTool = self._analyzeTools["MA"]
        maTool.setTimeperiod(period)
        maTool.setSourceData(self._KLineData.close.values)
        maTool.calculate()
        self._KLineData[col] = maTool.getResult()

    def _calculateMAX20(self):
        self._calculateMAX(20)

    def updateKLineData(self, kLineData):
        if self.concatKLineData(kLineData):
            return True
        else:
            return False

    def save2CSV(self,path):
        self._KLineData.to_csv(path)

    def save2DB(self):
        pass

    def getValueByIndex(self, index, kpiName):
        if 0 <= index <= self.getRowCount():
            try:
                return self._KLineData.loc[index, kpiName]
            except KeyError:
                print("index is " + str(index) + " and endindex is " + str(self.getRowCount()))
        else:
            return pd.np.nan

    def getRowCount(self):
        return self._KLineData.shape[0]

















