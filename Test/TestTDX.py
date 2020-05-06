from pytdx.hq import TdxHq_API
import pandas as pd

from AnalyzeTools.MACD import MACD
from Stock.AnalyseKLine import AnalyseKLine

api = TdxHq_API(auto_retry=True)
if api.connect('119.147.212.81', 7709):
    #dif =
    #if dif < 2:
    #    print("UUUUUUUUUUUUUUU:")
    data = api.to_df(api.get_index_bars(9, 1, '000905', 0, 500))  # 返回DataFrame
    ak = AnalyseKLine()
    ak.concatKLine(data)
    print("*" * 50)
    print(ak.getKLine())
    print("@@@@@@@@@@@@@@@@" + str(ak.getDataFragment()[len(ak.getDataFragment()) -1].getEIndex()))
    # print(data.high.values)
    print("*" * 50)

    data1 = api.to_df(api.get_index_bars(9, 1, '000905', 0, 1))# 返回DataFrame

    ak.concatKLine(data1)
    print("@@@@@@@@@@@@@@@@" + str(ak.getDataFragment()[len(ak.getDataFragment()) - 1].getEIndex()))

    # data.append(data1,ignore_index=True)

    print(ak.getKLine())
    api.disconnect()
quit()
