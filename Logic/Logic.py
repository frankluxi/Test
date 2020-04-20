from abc import abstractmethod


class Logic:
    # 计算逻辑ID
    _logicID = ""

    # 计算逻辑名称
    _logicName = ""

    # 计算逻辑描述
    _logicDesc = ""

    # 基础数据dataframe
    _data = None

    @abstractmethod
    def _doLogic(self):
        pass

    @abstractmethod
    def _doReverseLogic(self):
        pass

    # 执行计算逻辑， logic = 0 为正向逻辑  否则为反向逻辑   默认为计算正向逻辑
    def calLogic(self, data, logic=0):
        if data is None:
            print("invalid data")
            return None
        self._data = data
        if logic == 0:
            return self._doLogic()
        else:
            return self._doReverseLogic()

    # 执行计算逻辑， logic = 0 为正向逻辑  否则为反向逻辑   默认为计算正向逻辑
    def calLogic(self, logic=0):
        if self._data is None:
            print("invalid data")
            return None
        return self.calLogic(self._data, logic)

    def setLogicID(self, logicID):
        self._logicID = logicID

    def getLogicID(self):
        return self._logicID

    def setLogicName(self, logicName):
        self._logicName = logicName

    def getLogicName(self):
        return self._logicName

    def setLogicDesc(self, logicDesc):
        self._logicDesc = logicDesc

    def getLogicDesc(self):
        return self._logicDesc
