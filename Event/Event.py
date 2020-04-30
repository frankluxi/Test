from enum import Enum, unique


@unique
class EventType(Enum):
    UNKNOW = 0
    NEW_HIGH_DIF = 1
    NEW_LOW_DIF = 2
    NEW_HIGH_WL = 3
    NEW_LOW_WL = 4
    GOLDEN_FORK = 5
    DEAD_FORK = 6
    DIF_GT_0 = 7


class Event:
    _bIndex = -1

    _eIndex = -2

    _eventIndex = -1

    _eventType = EventType.UNKNOW

    _eventValue = None

    def setBIndex(self,bIndex):
        self._bIndex = bIndex

    def getBIndex(self):
        return self._bIndex

    def setEIndex(self,eIndex):
        self._eIndex = eIndex

    def getEIndex(self):
        return self._eIndex

    def setEventType(self,eventType):
        self._eventType = eventType

    def getEventType(self):
        return self._eventType

    def setEventValue(self,eventValue):
        self._eventValue = eventValue

    def getEventValue(self):
        return self._eventValue

    def setEventIndex(self,index):
        self._eventIndex = index

    def getEventIndex(self):
        return self._eventIndex

    def __eq__(self, other):
        return isinstance(other,Event) and self._eventType == other._eventType and self._eventIndex == other._eventIndex



