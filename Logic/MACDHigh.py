import sys

from Logic.OldLogic import OldLogic

from enum import Enum
from enum import unique


class MACDHigh(OldLogic):
    # 新高次数
    _achieveTimes = 3;

    __dataFragments = []

    def __init__(self):
        self._logicID = "0001"
        self._logicName = "MACD在0轴上出现N次新高"
        self._logicDesc = "DIF在0轴上出现N次新高"

    def setAchieveTimes(self,achieveTimes):
        self._achieveTimes = achieveTimes

    def getAchieveTimes(self):
        return self._achieveTimes

    def _doLogic(self):
        self.__calMaxMin()
        newHigCount = 0
        newHigh = 0
        for fragment in self.__dataFragments:
            if fragment.getMax() > newHigh:
                newHigCount += 1
                newHigh = fragment.getMax()
        if newHigCount >= self._achieveTimes:
            return True
        else:
            return False

    def _doReverseLogic(self):
        self.__calReverseMaxMin()
        newLowCount =  0
        newLow = sys.maxsize
        for fragment in self.__dataFragments:
            if fragment.getMin() < newLow:
                newLowCount += 1
                newLow = fragment.getMin()
        if newLowCount >= self._achieveTimes:
            return True
        else:
            return False

    def __difGT0Index(self):
        ret = self._data.shape[0] - 1;
        while ret > 0 and self._data.loc[ret, 'DIF'] > 0:
            ret -= 1;
        return ret;

    def __calMaxMin(self):
        print(self._data.columns)

        start = self._data.shape[0] - 1
        stockPillar = StockPillar.UNKNOW
        fragment = None
        dif = self._data.loc[start, 'DIF']
        dea = self._data.loc[start, 'DEA']
        while start > 0 and dif > 0:
            currentPillar = StockPillar.RED if dif - dea > 0 else StockPillar.GREEN
            if stockPillar == currentPillar:
                if stockPillar is StockPillar.RED:
                    if fragment.getMax() < dif:
                        fragment.setMax(dif)
                    if fragment.getMin() > dif:
                        fragment.setMin(dif)
            else:
                if stockPillar == StockPillar.UNKNOW:
                    if currentPillar == StockPillar.GREEN:
                        # 如果刚开始就是绿柱则退出
                        break;
                    fragment = DataFragment()
                    fragment.setEIndex(start)
                    fragment.setMax(dif)
                    fragment.setMin(dif)
                elif stockPillar == StockPillar.GREEN:
                    # 绿柱变红柱 重新计算新的红柱组起始和极值
                    fragment = DataFragment()
                    fragment.setEIndex(start)
                    fragment.setMax(dif)
                    fragment.setMin(dif)
                else:
                    # 红柱变绿
                    fragment.setBIndex(start + 1)
                    self.__dataFragments.index(0,fragment)
                    fragment = None
                # 置值红绿住状态 为最新状态
                stockPillar = currentPillar
            start -= 1
            dif = self._data.loc[start, 'DIF']
            dea = self._data.loc[start, 'DEA']
        if fragment is not None:
            self.__dataFragments.append(fragment)

    def __calReverseMaxMin(self):
        start = self._data.shape[0] - 1
        stockPillar = StockPillar.UNKNOW
        fragment = None
        dif = self._data.loc[start, 'DIF']
        dea = self._data.loc[start, 'DEA']
        while start > 0 and dif < 0:
            currentPillar = StockPillar.RED if dif - dea > 0 else StockPillar.GREEN
            if stockPillar == currentPillar:
                if stockPillar is StockPillar.RED:
                    if fragment.getMax() < dif:
                        fragment.setMax(dif)
                    if fragment.getMin() > dif:
                        fragment.setMin(dif)
            else:
                if stockPillar == StockPillar.UNKNOW:
                    if currentPillar == StockPillar.RED:
                        # 如果刚开始就是绿柱则退出
                        break;
                    fragment = DataFragment()
                    fragment.setEIndex(start)
                    fragment.setMax(dif)
                    fragment.setMin(dif)
                elif stockPillar == StockPillar.RED:
                    # 绿柱变红柱 重新计算新的红柱组起始和极值
                    fragment = DataFragment()
                    fragment.setEIndex(start)
                    fragment.setMax(dif)
                    fragment.setMin(dif)
                else:
                    # 红柱变绿
                    fragment.setBIndex(start + 1)
                    self.__dataFragments.insert(0,fragment)
                    fragment = None
                # 置值红绿住状态 为最新状态
                stockPillar = currentPillar
            start -= 1
            dif = self._data.loc[start, 'DIF']
            dea = self._data.loc[start, 'DEA']
        if fragment is not None:
            self.__dataFragments.append(fragment)
    def getDataFragment(self):
        return self.__dataFragments


@unique
class StockPillar(Enum):
    UNKNOW = 0
    RED = 1
    GREEN = 2




class DataFragment:

    __bIndex = -1

    __eIndex = -1

    __max = -1

    __min = -1

    def setBIndex(self,bIndex):
        self.__bIndex = bIndex

    def getBIndex(self):
        return self.__bIndex

    def setEIndex(self,eIndex):
        self.__eIndex = eIndex

    def getEIndex(self,eIndex):
        self.__eIndex = eIndex

    def setMax(self,max):
        self.__max = max

    def getMax(self):
        return self.__max

    def setMin(self,min):
        self.__min = min

    def getMin(self):
        return self.__min








