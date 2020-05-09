
from Event.Event import Event, EventType
from OldLogic.MACDHigh import StockPillar
from OldLogic.OldLogic import OldLogic


class OldDifNewHighLogic(OldLogic):
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








