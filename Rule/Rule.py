from abc import abstractmethod


class Rule:
    _strategyCode = "0000"
    _strategyName = ""
    _sourceData = None

    @abstractmethod
    def test(self):
        pass

    def setSourceData(self,sourceData):
        self._sourceData = sourceData

    def getStrategyCode(self):
        return  self._strategyCode

    def getStrategyName(self):
        return self._strategyName