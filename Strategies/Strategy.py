class Strategy:
    _strategyID = ""

    _strategyName = ""

    _strategyDesc = ""

    _rules = {}

    _data = None

    def setData(self,data):
        self._data = data

    def getData(self):
        return self._data

    def setStrategyID(self,strategyID):
        self._strategyID = strategyID

    def getStrategyID(self):
        return  self._strategyID

    def setStrategyName(self,strategyName):
        self._strategyName = strategyName

    def getStrategyName(self):
        return self._strategyName

    def setStrategyDesc(self,strategyDesc):
        self._strategyDesc = strategyDesc

    def getStrategyDesc(self):
        return self._strategyDesc
    def addRule(self,rule):
        # self._rules.update(rule.getRuleID(),rule)
        self._rules[rule.getRuleID()] = rule

    def removeLogic(self,ruleID):
        self._rules.pop(ruleID)

    def runStrategy(self):
        ret = True
        for value in self._rules.values():
            ret = ret and value.runRule(self._data)
            if not ret :
                break;
        return ret;