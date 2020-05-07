from enum import Enum, unique

import pandas as pd

from AnalyzeTools.MA import MA
from AnalyzeTools.MACD import MACD
from AnalyzeTools.MAX import MAX
from Logic.DIFNewHighLogic import DIFNewHighLogic


class AnalyseKLine:

    # 当前K线的起始索引
    __beginIndex = -1
    # 当前K线的截止索引
    __endIndex = -1
    # 本次K线更新的条数
    __updateRows = 0
    # 更新合并后K线的更新数据的起始索引
    __updateIndex = -1
    # 日线、15分钟线、30分钟线.......
    __KLineType = 0
    # K线数据，类型为DataFrame
    __KLineData = pd.DataFrame()
    # K线索引上发生的事件，类型为字典  key = index Value=事件列表
    __events = {}
    # K线的数据的索引片段
    __fragments = []

    __analyzeTools = {}

    __logics = ["DIFNewHighLogic"]

    def __init__(self):
        self.__analyzeTools.update({'MA': MA(None)})
        self.__analyzeTools.update({'MACD': MACD(None)})
        self.__analyzeTools.update({'MAX': MAX(None)})

    def __calculateMA5(self):
        self.__calculateMA(5)

    #10日均线
    #@abstractmethod
    def __calculateMA10(self):
        self.__calculateMA(10)

    #20日均线
    #@abstractmethod
    def __calculateMA20(self):
        self.__calculateMA(20)

    #30日均线
    #@abstractmethod
    def __calculateMA30(self):
        self.__calculateMA(30)


    #60日均线
    #@abstractmethod
    def __calculateMA60(self):
        self.__calculateMA(60)

    #120日均线
    #@abstractmethod
    def __calculateMA120(self):
        self.__calculateMA(120)

    #250日均线
    #@abstractmethod
    def __calculateMA250(self):
        self.__calculateMA(250)

    def __calculateMACD(self,fastperiod = 12,slowperiod = 26,signalperiod = 9):
        macdTool = self.__analyzeTools["MACD"]
        macdTool.setFastPeriod(fastperiod)
        macdTool.setSlowPeriod(slowperiod)
        macdTool.setSignalPeriod(signalperiod)
        macdTool.setSourceData(self.__KLineData.close.values)
        macdTool.calculate()
        self.__KLineData['DIF'] = macdTool.getDiff()
        self.__KLineData['DEA'] = macdTool.getDea();

    def __calculateMA(self,period):
        col = 'MA' + str(period);
        maTool = self.__analyzeTools["MA"]
        maTool.setTimeperiod(period)
        maTool.setSourceData(self.__KLineData.close.values)
        maTool.calculate()
        self.__KLineData[col] = maTool.getResult()

    def __calculateMAX20(self):
        self.__calculateMAX(20)

    def __calculateMAX(self,period):
        col = 'MAX' + str(period);
        maxTool = self.__analyzeTools["MAX"]
        maxTool.setTimeperiod(period)
        maxTool.setSourceData(self.__KLineData.close.values)
        maxTool.calculate()
        self.__KLineData[col] = maxTool.getResult()

    def concatKLine(self, KLineData):
        if isinstance(KLineData, pd.DataFrame):
            # 合并两个dataframe
            self.__KLineData = pd.concat([self.__KLineData, KLineData], axis=0, ignore_index=True)
            # 重新计算衍生指标
            self.__calculateMA5()
            self.__calculateMA10()
            self.__calculateMA20()
            self.__calculateMA30()
            self.__calculateMA60()
            self.__calculateMA120()
            self.__calculateMA250()
            self.__calculateMACD()
            self.__calculateMAX20()
            updateRows = KLineData.shape[0]
            # 有数据更新
            if updateRows > 0:
                self.__beginIndex = 0
                self.__updateIndex = self.__endIndex + 1
                self.__endIndex = self.__KLineData.shape[0]
                self.__updateFragments()
                index = self.__updateIndex
                while index < self.__endIndex:
                    self.__calLogics(index)
                    index += 1
            return True
        else:
            print("invalid param")
            return False

    def addEvent(self, index, event):
        indexEvent = self.__events[index]
        if self.containsEvent(index, event):
            indexEvent.remove(event)
        indexEvent.append(event)

    def containsEvent(self, index, event):
        return event in self.__events[index]
    # 返回当前的K线
    def getKLine(self):
        return self.__KLineData

    # 根据K线更新红绿柱组Datafragment信息
    def __updateFragments(self):
        length = len(self.__fragments)
        # K线总行数
        rows = self.__KLineData.shape[0]
        # 如果Datafragment没有信息则说明此组K线没有被快照过Datafragment
        start = 0 if length == 0 else self.__fragments[length - 1].getEIndex() + 1
        if start >= rows:
            return
        # 初始化Datafragment  如果datafragment中没有任何元素则为None否则取最后元素
        fragment = None if length == 0 else self.__fragments[length - 1]
        stockPillar = StockPillar.UNKNOW if fragment is None else fragment.getStockPillar()
        while start < rows:
            dif = self.getDifByIndex(start)
            dea = self.getDeaByIndex(start)
            currPillar = StockPillar.RED if dif - dea > 0 else StockPillar.GREEN
            if stockPillar == currPillar:
                if fragment.getMax() < dif:
                    fragment.setMax(dif)
                if fragment.getMin() > dif:
                    fragment.setMin(dif)
            else:
                if fragment is not None:
                    fragment.setEIndex(start)
                    self.__insertFragment(fragment)
                fragment = self.__newFragment(stockPillar, start, -1, dif)
                stockPillar = currPillar
            start += 1

        if fragment.getEIndex() != start:
            fragment.setEIndex(start - 1)
            self.__insertFragment(fragment)

    def getValueByIndex(self,index,kpiName):
        # 需要容错处理
        if index >= self.__beginIndex and index <= self.__endIndex:
            return self.__KLineData.loc[index, kpiName]
        else:
            return None

    def getDifByIndex(self,index):
        return self.getValueByIndex(index,'DIF')

    def getDeaByIndex(self,index):
        return self.getValueByIndex(index,'DEA')

    def getCloseByIndex(self,index):
        return self.getValueByIndex(index,'close')

    def getOpenByIndex(self,index):
        return self.getValueByIndex(index,'open')

    def getHighByIndex(self,index):
        return self.getValueByIndex(index,'high')

    def getLowByIndex(self,index):
        return self.getValueByIndex(index,'low')

    def getVolByIndex(self,index):
        return self.getValueByIndex(index,'vol')

    def getAmountByIndex(self,index):
        return self.getValueByIndex(index,'amount')

    def __newFragment(self,stockPillar,bIndex,eIndex,value):
        fragment = DataFragment()
        fragment.setBIndex(bIndex)
        fragment.setEIndex(eIndex)
        fragment.setMax(value)
        fragment.setMin(value)
        fragment.setStockPillar(stockPillar)
        return fragment

    def __insertFragment(self,fragment):
        if not fragment in self.__fragments:
            self.__fragments.append(fragment)

    def getDataFragments(self):
        return self.__fragments

    def getDataFragmentByIndex(self,index):
        ret = None
        for datafragment in self.__fragments:
            if datafragment.getBIndex() <= index and datafragment.getEIndex() >= index:
                ret = datafragment
                break
        return ret
    # 判断指定索引是否存在指定类型的事件，如果存在返回该事件实例否则返回空
    def getEventByType(self,index,eventType):
        ret = None
        try:
            events = self.__events[index]
        except KeyError:
            pass
        else:
            for event in events:
                if event.getEventType() == eventType:
                    ret = event
                    break
        return ret

    # 根据逻辑名字进行逻辑计算，符合条件则产生事件否则返回None
    def __calLogic(self,logicName,index):
        package = __import__("Logic")
        module = getattr(package, logicName)
        logic_class = getattr(module, logicName)
        logic = logic_class(index,self)
        return logic.calculateLogic()

    def __calLogics(self,index):
        for logicName in self.__logics:
            event = self.__calLogic(logicName,index)
            # 如果逻辑计算产生了事件，则将此事件
            if event is not None:
                self.__events.setdefault(index,[]).append(event)








@unique
class StockPillar(Enum):
    UNKNOW = 0
    RED = 1
    GREEN = 2




class DataFragment:

    __bIndex = -1

    __eIndex = -1

    __max = -1

    __min = -1

    __stockPillar = StockPillar.UNKNOW

    def setBIndex(self,bIndex):
        self.__bIndex = bIndex

    def getBIndex(self):
        return self.__bIndex

    def setEIndex(self,eIndex):
        self.__eIndex = eIndex

    def getEIndex(self):
        return self.__eIndex

    def setMax(self,max):
        self.__max = max

    def getMax(self):
        return self.__max

    def setMin(self,min):
        self.__min = min

    def getMin(self):
        return self.__min

    def setStockPillar(self,stockPillar):
        self.__stockPillar = stockPillar

    def getStockPillar(self):
        return self.__stockPillar

    def __eq__(self, other):
        return isinstance(other,DataFragment) and self.__bIndex == other.__bIndex and self.__eIndex == other.__eIndex