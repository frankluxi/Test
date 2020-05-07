from Logic.OldLogic import OldLogic
from Logic.MACDHigh import MACDHigh


class MACDdbl(OldLogic):
    _achieveTimes = 2

    def __init__(self):
        self._logicID = "0002"
        self._logicName = "MACD在0轴上出现N次新高后的顶背离"
        self._logicDesc = "MACD在0轴上出现N次新高后的顶背离"

    def _doLogic(self):
        macdHigh = MACDHigh()
        macdHigh.setAchieveTimes(self._achieveTimes)


    def _doReverseLogic(self):
        pass