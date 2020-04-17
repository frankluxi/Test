from abc import abstractmethod


class AnalyzeTool:
    _sourceData = None
    _result = None
    def __init__(self,sourceData):
        self.setSourceData(sourceData)

    def setSourceData(self,sourceData):
        self._sourceData = sourceData
    @abstractmethod
    def calculate(self):
        print("GGGG")
        pass

    def getResult(self):
        return self._result

    def setResult(self,result):
        self._result = result
