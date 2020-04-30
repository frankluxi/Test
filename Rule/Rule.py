from abc import abstractmethod


class Rule:
    # 规则编码
    _ruleID = "0000"

    # 规则名称
    _ruleName = ""

    # 基础数据
    _data = None

    # 计算逻辑
    _logics = {}

    # 次方法在基类中做了默认实现，对于每一个logic而言都是与的关系形成最后的规则运行结果，
    # 因此字类如果有不是与关系的规则需要override此方法  @abstractmethod
    def _runRule(self):
        ret = True
        for value in self._logics.values():
            ret = ret and value.calLogic(self._data,logic=0)
            if not ret:
                break;
        return ret;

    # 次方法在基类中做了默认实现，对于每一个logic而言都是与的关系形成最后的规则运行结果，
    # 因此字类如果有不是与关系的规则需要override此方法  @abstractmethod
    def runRule(self,data):
        self._data = data
        return self._runRule()




    def setSourceData(self,data):
        self._data = data

    def getStrategyCode(self):
        return  self._ruleID

    def getStrategyName(self):
        return self._ruleName

    def addLogic(self,logic):
        # self._logics.update(logic.getLogicID(),logic)
        self._logics[logic.getLogicID()] = logic

    def removeLogic(self,logicID):
        self._logics.pop(logicID)

    def setRuleID(self,ruleID):
        self._ruleID = ruleID

    def getRuleID(self):
        return self._ruleID

    def setRuleName(self,ruleName):
        self._ruleName = ruleName

    def getRuleName(self):
        return self._ruleName