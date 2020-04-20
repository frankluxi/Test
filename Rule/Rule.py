from abc import abstractmethod


class Rule:
    # 规则编码
    _ruleCode = "0000"

    # 规则名称
    _ruleName = ""

    # 基础数据
    _data = None

    @abstractmethod
    def runRule(self):
        pass

    def setSourceData(self,data):
        self._data = data

    def getStrategyCode(self):
        return  self._ruleCode

    def getStrategyName(self):
        return self._ruleName