from Event.Event import Event, EventType
from Logic.Logic import Logic
import math


class HighestLogic(Logic):

    __duration = 20

    def setDuration(self,duration):
        self.__duration = duration

    def getDuration(self):
        return self.__duration

    def __init__(self, index, analyseKLine):
        super().__init__(index, analyseKLine)
        self._logicID = "00004"
        self._logicName = "持续事件的最高值"
        self._logicDesc = "前后duration中的最高值"

    def _getBeginIndex(self):
        return self._index

    def _getEndIndex(self):
        return self._index

    def _doLogic(self, index):
        ret = None
        # if self._index - self.__duration >= 0:
        highestIndex = self._index - self.__duration  # math.ceil(self._index / 2)
        highestValue = self._analyseKLine.getHighByIndex(highestIndex)
        step = 1
        isHighest = True
        while step <= self.__duration:
            if highestValue < self._analyseKLine.getHighByIndex(highestIndex - step) or highestValue < self._analyseKLine.getHighByIndex(highestIndex + step):
                isHighest = False
                break
            step += 1
        if isHighest:
            ret = Event()
            ret.setBIndex(highestIndex - step)
            ret.setEIndex(highestIndex + step)
            ret.setEventIndex(highestIndex)
            ret.setEventType(self.__getHighEventType())
            ret.setEventValue(highestValue)
        return ret

    def _doReverseLogic(self):
        pass

    def __getHighEventType(self):
        ret = None
        if self.__duration == 20:
            ret = EventType.HIGHEST_20
        elif self.__duration == 30:
            ret = EventType.HIGHEST_30
        else:
            ret = EventType.HIGHEST_20
        return ret

    def __getLowEventType(self):
        ret = None
        if self.__duration == 20:
            ret = EventType.LOWEST_20
        elif self.__duration == 30:
            ret = EventType.LOWEST_30
        else:
            ret = EventType.LOWEST_20
        return ret





