from abc import ABCMeta, abstractmethod


class KLineInterface(object):
    # 抽象类
    __metaclass__ = ABCMeta

    @abstractmethod
    def getValueByIndex(self, index, kpiName):
        pass

    @abstractmethod
    def getDifByIndex(self, index):
        pass

    @abstractmethod
    def getDeaByIndex(self, index):
        pass

    @abstractmethod
    def getCloseByIndex(self, index):
        pass

    @abstractmethod
    def getOpenByIndex(self, index):
        pass

    @abstractmethod
    def getHighByIndex(self, index):
        pass

    @abstractmethod
    def getLowByIndex(self, index):
        pass

    @abstractmethod
    def getVolByIndex(self, index):
        pass

    @abstractmethod
    def getAmountByIndex(self, index):
        pass

    @abstractmethod
    def updateKLineData(self,kLineData):
        pass

    @abstractmethod
    def concatKLineData(self,kLineData):
        pass

    @abstractmethod
    def save2CSV(self,path):
        pass

    @abstractmethod
    def save2DB(self):
        pass

    @abstractmethod
    def getData(self):
        pass
