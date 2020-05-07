from Event.Event import Event, EventType
from Logic.Logic import Logic
import sys


class DIFNewHighLogic(Logic):

    __dif = 0

    __difNewHigh = -sys.float_info.max

    def __init__(self, index, analyseKLine):
        super().__init__(index, analyseKLine)
        self._logicID = "00001"
        self._logicName = "DIF 0 轴上新高逻辑"
        self._logicDesc = "DIF 在0轴上出现的新高"
        self.__dif = self._analyseKLine.getDifByIndex(index)

    def _getBeginIndex(self):
        if self.__dif > 0:
            index = self._index
            while self._analyseKLine.getDifByIndex(index) > 0:
                index -= 1
            return index + 1
        else:
            return -1

    def _getEndIndex(self):
        if self.__dif > 0:
            return self._index
        else:
            return -1

    def _doLogic(self, index):
        ret = None
        difIndex = self._analyseKLine.getDifByIndex(index)
        if self.__difNewHigh < difIndex:
            if index == self._index:
                ret = Event()
                ret.setBIndex(index)
                ret.setEIndex(index)
                ret.setEventIndex(index)
                ret.setEventType(EventType.NEW_HIGH_DIF)
                ret.setEventValue(difIndex)
            self.__difNewHigh = difIndex
        return ret
