from abc import ABCMeta, abstractmethod




class StockBase:
    #股票编号
    _stockCode = ""
    #股票名称
    _stockName = ""
    #分析天数
    _stockOberCount = 300
    #K线数据  dataframe
    _KLineData = None
    #分析工具 如MA  MACD  MAX。。。。。
    _analyzeTools = {}

    _strategies = []

    def __calculateMAX(self,period):
        col = 'MAX' + str(period);
        maxTool = self._analyzeTools["MAX"]
        maxTool.setTimeperiod(period)
        maxTool.setSourceData(self._KLineData.close.values)
        maxTool.calculate()
        self._KLineData[col] = maxTool.getResult()
        #print(self._KLineData)
        #print(self._KLineData.loc[self._KLineData.shape[0] -1,'MA250'])


    def __calculateMA(self,period):
        col = 'MA' + str(period);
        maTool = self._analyzeTools["MA"]
        maTool.setTimeperiod(period)
        maTool.setSourceData(self._KLineData.close.values)
        maTool.calculate()
        self._KLineData[col] = maTool.getResult()
        #print(self._KLineData)

    @abstractmethod
    def _getKLineData(self):
        pass
    #5日均线

    def _calculateMA5(self):
        self.__calculateMA(5)

    #10日均线
    #@abstractmethod
    def _calculateMA10(self):
        self.__calculateMA(10)

    #20日均线
    #@abstractmethod
    def _calculateMA20(self):
        self.__calculateMA(20)

    #30日均线
    #@abstractmethod
    def _calculateMA30(self):
        self.__calculateMA(30)


    #60日均线
    #@abstractmethod
    def _calculateMA60(self):
        self.__calculateMA(60)

    #120日均线
    #@abstractmethod
    def _calculateMA120(self):
        self.__calculateMA(120)

    #250日均线
    #@abstractmethod
    def _calculateMA250(self):
        self.__calculateMA(250)

    def _calculateMACD(self,fastperiod = 12,slowperiod = 26,signalperiod = 9):
        macdTool = self._analyzeTools["MACD"]
        macdTool.setFastPeriod(fastperiod)
        macdTool.setSlowPeriod(slowperiod)
        macdTool.setSignalPeriod(signalperiod)
        macdTool.setSourceData(self._KLineData.close.values)
        macdTool.calculate()
        self._KLineData['DIF'] = macdTool.getDiff()
        self._KLineData['DEA'] = macdTool.getDea();
        # print(self._KLineData)

    def _calculateMAX20(self):
        self.__calculateMAX(20)


    def _calculateAllIndex(self):
        if self._KLineData == None:
            print("请先获取K线数据")
            return
        for key,ind in self._analyzeTools.items():
            ind.setSourceData(self._KLineData.close.values)
            ind.calculate()

    def _toolsNeedUpdate(self):
        for key,ind in self._analyzeTools.items():
            ind.setResult(None)

    def setStockCode(self,stockCode):
        self._stockCode = stockCode;

    def getStockCode(self):
        return self._stockCode

    def setStockName(self,stockName):
        self._stockName = stockName

    def getStockName(self):
        return self._stockName

    def getKLineData(self):
        return self._KLineData

    def addMATool(self,MA):
        self._analyzeTools.update({'MA': MA})

    def addMACDTool(self,MACD):
        self._analyzeTools.update({'MACD': MACD})

    def addMAXTool(self,MAX):
        self._analyzeTools.update({'MAX': MAX})

    def addStrategy(self,strategy):
        self._strategies.append(strategy)

    def runStategies(self):
        for strategy in self._strategies:
            print("now is running Rule name = " + strategy.getStrategyName() + "......")
            strategy.setData(self._KLineData)
            ret = strategy.runStrategy()
            print("now Rule name = " + strategy.getStrategyName() + " run over the result = " + str(ret))

    def loadKLineData(self):
        self._getKLineData()
        #print(self._KLineData)
        self._calculateMA5()
        #print(self._KLineData)
        self._calculateMA10()
        self._calculateMA20()
        self._calculateMA30()
        self._calculateMA60()
        self._calculateMA120()
        self._calculateMA250()
        self._calculateMACD()
        self._calculateMAX20()





