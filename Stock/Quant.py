from Stock.KLine import KLineType, KLine
from Stock.MACDFragment import MACDFragment, StockPillar


class Quant(object):

    __klineType__ = KLineType.LINE_UNKNOW

    __kline__ = None

    __MACDFragments__ = []

    def __init__(self, klineType):
        self.__klineType__ = klineType
        self.__kline__ = KLine(self.__klineType__)

    def udateKLine(self, kLineData):
        self.__kline__.updateKLineData(kLineData)
        # 更新红绿柱段
        length = len(self.__MACDFragments__)
        rows = self.__kline__.getRowCount()#self.__kline__.shape[0]
        # 如果Datafragment没有信息则说明此组K线没有被快照过Datafragment
        start = 0 if length == 0 else self.__MACDFragments__[length - 1].getEIndex() + 1
        self.__updateMACDFraments(start,rows - 1)

    def __updateMACDFraments(self,fromIndex,toIndex):
        if fromIndex >= toIndex:
            return
        length = len(self.__MACDFragments__)
        # 初始化Datafragment  如果datafragment中没有任何元素则为None否则取最后元素
        fragment = None if length == 0 else self.__MACDFragments__[length - 1]
        stockPillar = StockPillar.UNKNOW if fragment is None else fragment.getStockPillar()
        while fromIndex <= toIndex:
            dif = self.__kline__.getDifByIndex(fromIndex)
            dea = self.__kline__.getDeaByIndex(fromIndex)
            currPillar = StockPillar.RED if dif - dea > 0 else StockPillar.GREEN
            if stockPillar == currPillar:
                if fragment.getMax() < dif:
                    fragment.setMax(dif)
                if fragment.getMin() > dif:
                    fragment.setMin(dif)
            else:
                if fragment is not None:
                    fragment.setEIndex(fromIndex)
                    self.__insertFragment(fragment)
                fragment = self.__newFragment(stockPillar, fromIndex, -1, dif)
                stockPillar = currPillar
            fromIndex += 1

        if fragment.getEIndex() != fromIndex:
            fragment.setEIndex(fromIndex - 1)
            self.__insertFragment(fragment)

    # 构造一个新的MACDFragment
    def __newFragment(self, stockPillar, bIndex, eIndex, value):
        fragment = MACDFragment()
        fragment.setBIndex(bIndex)
        fragment.setEIndex(eIndex)
        fragment.setMax(value)
        fragment.setMin(value)
        fragment.setStockPillar(stockPillar)
        return fragment

    def __insertFragment(self, fragment):
        if not fragment in self.__MACDFragments__:
            self.__MACDFragments__.append(fragment)

    def getKLine(self):
        return self.__kline__

    def printFragment(self):
        length = len(self.__MACDFragments__)
        # 初始化Datafragment  如果datafragment中没有任何元素则为None否则取最后元素
        fragment = None if length == 0 else self.__MACDFragments__[length - 1]
        print(fragment.getEIndex())
