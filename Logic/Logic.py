from abc import abstractmethod


class Logic:
    # 计算逻辑ID
    _logicID = ""

    # 计算逻辑名称
    _logicName = ""

    # 计算逻辑描述
    _logicDesc = ""

    # 对应的当前K线Index
    _index = -1

    # K线分析对象
    _analyseKLine = None

    def __init__(self, index, analyseKLine):
        self._index = index
        self._analyseKLine = analyseKLine

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

    def setIndex(self,index):
        self._index = index

    def getIndex(self):
        return self._index

    @abstractmethod
    def _getBeginIndex(self):
        pass

    @abstractmethod
    def _getEndIndex(self):
        pass

    @abstractmethod
    def _doLogic(self,index):
        pass

    def calculateLogic(self):
        currIndex = self._getBeginIndex()
        end = self._getEndIndex()
        ret = None
        while currIndex != -1 and end != -1 and currIndex <= end :
            ret = self._doLogic(currIndex)
            if ret is not None:
                break
            currIndex += 1
        return ret

    def setAnalyseKLine(self,analyseKLine):
        self._analyseKLine = analyseKLine


