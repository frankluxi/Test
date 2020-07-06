
from pytdx.hq import TdxHq_API
import pandas as pd
import datetime


from Event.Event import EventType
from Stock.AnalyseKLine import AnalyseKLine
#dd = DIFNewHighLogic()
from Stock.KLine import KLine, KLineType
from Stock.Quant import Quant

api = TdxHq_API(auto_retry=True)
if api.connect('119.147.212.81', 7709):
    data = api.to_df(api.get_index_bars(9, 1, '000905', 0, 500))  # 返回DataFrame
    start = datetime.datetime.now()
    quant = Quant(KLineType.LINE_1_D)
    quant.udateKLine(data)
    end = datetime.datetime.now()
    print(end - start)
    print("*" * 50)
    print(quant.getKLine().getData())
    quant.printFragment()
    print("*" * 50)

    api.disconnect()
quit()