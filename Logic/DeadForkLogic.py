from Event.Event import Event, EventType
from Logic.Logic import Logic


class DeadForkLogic(Logic):
    def __init__(self, index, analyseKLine):
        super().__init__(index, analyseKLine)
        self._logicID = "00002"
        self._logicName = "死叉逻辑"
        self._logicDesc = "上一个周期dif-dea>0 当前周期dif - dea<0 "

    def _getBeginIndex(self):
        return self._index

    def _getEndIndex(self):
        return self._index

    def _doLogic(self, index):
        lastValue = self._analyseKLine.getDifByIndex(index - 1) - self._analyseKLine.getDeaByIndex(index - 1)
        value = self._analyseKLine.getDifByIndex(index) - self._analyseKLine.getDeaByIndex(index)
        ret = None
        if lastValue >0 and value < 0:
            ret = Event()
            ret.setBIndex(index)
            ret.setEIndex(index)
            ret.setEventIndex(index)
            ret.setEventType(EventType.DEAD_FORK)
            ret.setEventValue(value)
        return ret

    def _doReverseLogic(self):
        pass


