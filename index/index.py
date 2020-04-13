class Index:
    _sourceData = None

    def __init__(self,sourceData):
        self.__sourceData = sourceData

    def setSourceData(self,sourceData):
        self.__sourceData = sourceData
    @abstractmethod
    def calculate(self):
        print("GGGG")
        pass
