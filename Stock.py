from index.MacdClass import MACD
import tushare as tu


class Stock:
    __stockID = ""
    __stockName = ""
    __Macd = MACD
    __MA = None

    def __init__(self, stockID):
        self.__stockID = stockID
        self.__loadKLine()

    def __loadKLine(self):
        self.__kLine = tu.get_k_data(self.__stockID)


    def calMacd(self):
        if self.__kLine is None:
            print("请先获取K线数据")
        close = self.__kLine.close.values
        self.__Macd = MACD(close)
        self.__Macd.exec();

    def printDiff(self):
        if self.__Macd is None:
            print("请先获计算MACD")
        print(self.__Macd.getDiff())
        print(type(self.__Macd.getDiff()))

    def getStockName(self):
        return self.__stockName





stock = Stock("002142")
stock.calMacd()
stock.printDiff()
