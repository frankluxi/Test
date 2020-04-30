from enum import Enum, unique

from Event.Event import Event, EventType
from Logic.Logic import Logic


class DifNewHighLogic(Logic):
    __dataFragments = []



    def __init__(self, index, data):
        super().__init__(index, data)

    def _doLogic(self):
        ret = None
        self.__calFragments()
        newHigh = 0
        for fragment in self.__dataFragments:
            if fragment.getStockPillar() == StockPillar.RED:
                if fragment.getMax() > newHigh:
                    ret = Event()
                    ret.getEventType(EventType.NEW_HIGH_DIF)
                    ret.setBIndex(fragment.getBIndex)
                    ret.setEIndex(fragment.getEIndex())
                    ret.getEventValue(fragment.getMax())
                    ret.setEventIndex(self._currentIndex)
                    break;
        return ret



    def _doReverseLogic(self):
        pass

    def _isBeginIndex(self, index):
        return self._currentIndex == index

    def _isEndIndex(self, index):
        kData = self._data.getKLine()
        return True if kData.loc[index, 'DIF'] < 0 else False

    def __calFragments(self):
        start = self._currentIndex
        dif = self._data.loc[start, 'DIF']
        dea = self._data.loc[start, 'DEA']
        stockPillar = StockPillar.RED if dif - dea > 0 else StockPillar.GREEN
        # if stockPillar == StockPillar.GREEN:
        #     return
        fragment = self.newFragment(stockPillar,start,dif)
        while not self._isEndIndex(start):
            currentPillar = StockPillar.RED if dif - dea > 0 else StockPillar.GREEN
            if currentPillar == stockPillar:
                if fragment.getMax() < dif:
                    fragment.setMax(dif)
                if fragment.getMin() > dif:
                    fragment.setMin(dif)
            else:
                fragment.setBIndex(start - 1)
                self.__dataFragments.insert(0,fragment)
                fragment = self.newFragment(currentPillar,start,dif)
                stockPillar = currentPillar
            start += 1
            dif = self._data.loc[start, 'DIF']
            dea = self._data.loc[start, 'DEA']
        if -1 == fragment.getBIndex():
            fragment.setBIndex(start - 1)
            self.__dataFragments.insert(0,fragment)


    def newFragment(self,stockPillar,index,dif):
        fragment = DataFragment()
        fragment.setEIndex(index)
        fragment.setMax(dif)
        fragment.setMin(dif)
        fragment.setStockPillar(stockPillar)
        return fragment


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

    __stockPillar = StockPillar.UNKNOW

    def setBIndex(self,bIndex):
        self.__bIndex = bIndex

    def getBIndex(self):
        return self.__bIndex

    def setEIndex(self,eIndex):
        self.__eIndex = eIndex

    def getEIndex(self):
        return self.__eIndex

    def setMax(self,max):
        self.__max = max

    def getMax(self):
        return self.__max

    def setMin(self,min):
        self.__min = min

    def getMin(self):
        return self.__min

    def setStockPillar(self,stockPillar):
        self.__stockPillar = stockPillar

    def getStockPillar(self):
        return self.__stockPillar
