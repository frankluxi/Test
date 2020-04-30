import pandas as pd

class AnalyseKLine:

    __KLineType = 0
    __KLineData = pd.DataFrame()

    __events = {}

    def concatKLine(self,KLineData):
        if isinstance(KLineData, pd.DataFrame):
            self.__KLineData = pd.concat([self.__KLineData, KLineData], axis=0, ignore_index=True)
            return True
        else:
            print("invalid param")
            return False

    def addEvent(self,index,event):
        indexEvent = self.__events[index]
        if indexEvent.
        indexEvent.append(event)

    def containsEvent(self,index ,event):
        return self.__events[index].contains(event)

    def getKLine(self):
        return self.__KLineData
