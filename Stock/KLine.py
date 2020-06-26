from enum import Enum, unique

import pandas as pd

from Stock.AbstractKLine import AbstractKline


@unique
class KLineType(Enum):
    LINE_1_D = 0
    LINE_15_M = 1
    LINE_30_M = 2


class KLine(AbstractKline):
    __KLineType = KLineType.LINE_1_D
    # # K线数据，类型为DataFrame
    # _KLineData = pd.DataFrame()

    def __init__(self, kLineType):
        super(KLine,self).__init__()
        self.__KLineType = kLineType

    def concatKLineData(self, kLineData):
        if isinstance(kLineData, pd.DataFrame):
            # 合并两个dataframe
            self._KLineData = pd.concat([self._KLineData, kLineData], axis=0, ignore_index=True)
            # 重新计算衍生指标
            self._calculateMA5()
            self._calculateMA10()
            self._calculateMA20()
            self._calculateMA30()
            self._calculateMA60()
            self._calculateMA120()
            self._calculateMA250()
            self._calculateMACD()
            self._calculateMAX20()
            return True
        else:
            print("invalid param")
            return False

    def getDifByIndex(self, index):
        return self.getValueByIndex(index, 'DIF')

    def getDeaByIndex(self, index):
        return self.getValueByIndex(index, 'DEA')

    def getCloseByIndex(self, index):
        return self.getValueByIndex(index, 'close')

    def getOpenByIndex(self, index):
        return self.getValueByIndex(index, 'open')

    def getHighByIndex(self, index):
        return self.getValueByIndex(index, 'high')

    def getLowByIndex(self, index):
        return self.getValueByIndex(index, 'low')

    def getVolByIndex(self, index):
        return self.getValueByIndex(index, 'vol')

    def getAmountByIndex(self, index):
        return self.getValueByIndex(index, 'amount')
