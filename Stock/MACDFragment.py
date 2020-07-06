from enum import unique, Enum


@unique
class StockPillar(Enum):
    UNKNOW = 0
    RED = 1
    GREEN = 2


class MACDFragment:
    __bIndex = -1

    __eIndex = -1

    __max = -1

    __min = -1

    __stockPillar = StockPillar.UNKNOW

    def setBIndex(self, bIndex):
        self.__bIndex = bIndex

    def getBIndex(self):
        return self.__bIndex

    def setEIndex(self, eIndex):
        self.__eIndex = eIndex

    def getEIndex(self):
        return self.__eIndex

    def setMax(self, max):
        self.__max = max

    def getMax(self):
        return self.__max

    def setMin(self, min):
        self.__min = min

    def getMin(self):
        return self.__min

    def setStockPillar(self, stockPillar):
        self.__stockPillar = stockPillar

    def getStockPillar(self):
        return self.__stockPillar

    def __eq__(self, other):
        return isinstance(other, MACDFragment) and self.__bIndex == other.__bIndex and self.__eIndex == other.__eIndex
