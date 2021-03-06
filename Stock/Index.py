from pytdx.hq import TdxHq_API

from Stock.Stockbase import StockBase
from AnalyzeTools.MA import MA
from AnalyzeTools.MACD import MACD
from AnalyzeTools.MAX import MAX



from Strategies.StrategyTest import TestStrategy


class Index(StockBase):

    def __init__(self,stockCode):
        self._stockCode = stockCode

    def _getKLineData(self):
        api = TdxHq_API(auto_retry=True)
        if api.connect('119.147.212.81', 7709):
            self._KLineData = api.to_df(api.get_index_bars(9, 1, self._stockCode, 0, self._stockOberCount))  # 返回DataFrame
            # print(self._KLineData)
            api.disconnect()


hs500 = Index("000905")
hs500.addMATool(MA(None))
hs500.addMACDTool(MACD(None))
hs500.addMAXTool(MAX(None))

hs500.loadKLineData()
hs500.addStrategy(TestStrategy())
hs500.runStategies()


