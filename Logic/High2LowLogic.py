from Event.Event import Event, EventType
from Logic.Logic import Logic
import Stock.AnalyseKLine as ak


class High2LowLogic(Logic):
    def __init__(self, index, analyseKLine):
        super().__init__(index, analyseKLine)
        self._logicID = "00003"
        self._logicName = "新高拉低逻辑"
        self._logicDesc = "上一个红柱组中出现DIF新高，在接下来的一个红柱组中最高点没有达到上一个红柱组的最高点"

    def _getBeginIndex(self):
        return self._index

    def _getEndIndex(self):
        return self._index

    def _doLogic(self, index):
        lastValue = self._analyseKLine.getDifByIndex(index - 1) - self._analyseKLine.getDeaByIndex(index - 1)
        value = self._analyseKLine.getDifByIndex(index) - self._analyseKLine.getDeaByIndex(index)
        ret = None
        if lastValue > 0 and value < 0:  # 此处肯定为绿柱的起始点
            dataFragment = self._analyseKLine.getDataFragmentByIndex(index)
            if dataFragment is None:
                raise IndexError
            fragmentIndex = self._analyseKLine.getDataFragments().index(dataFragment)
            if fragmentIndex >= 3: # 至少要有两组红柱，计算逻辑才能产生事件
                dataFragment1 = self._analyseKLine.getDataFragments()[fragmentIndex - 1]
                dataFragment2 = self._analyseKLine.getDataFragments()[fragmentIndex - 3]  # 1和3 为相邻两组红柱
                if dataFragment1.getStockPillar() != ak.StockPillar.RED or dataFragment2.getStockPillar() != ak.StockPillar.RED:
                    # 此两组fragment一定为红柱否则整个K线是错误的
                    raise Exception("Stock Pillar Error!", index)
                if dataFragment1.getMax() < dataFragment2.getMax():
                    ret = Event()
                    ret.setBIndex(index)
                    ret.setEIndex(index)
                    ret.setEventIndex(index)
                    ret.setEventType(EventType.HIGH_TO_LOW)
                    ret.setEventValue(value)

