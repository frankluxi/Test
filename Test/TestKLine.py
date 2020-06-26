from pytdx.hq import TdxHq_API
import pandas as pd
import datetime


from Event.Event import EventType
from Stock.AnalyseKLine import AnalyseKLine
#dd = DIFNewHighLogic()
from Stock.KLine import KLine, KLineType

api = TdxHq_API(auto_retry=True)
if api.connect('119.147.212.81', 7709):
    data = api.to_df(api.get_index_bars(9, 1, '000905', 0, 500))  # 返回DataFrame
    start = datetime.datetime.now()
    ak = KLine(KLineType.LINE_1_D)
    ak.updateKLineData(data)
    end = datetime.datetime.now()
    print(end - start)
    print("*" * 50)
    print(ak.getData())
    print("*" * 50)

    api.disconnect()
quit()