from pytdx.hq import TdxHq_API
import pandas as pd
import datetime


from Event.Event import EventType
from Stock.AnalyseKLine import AnalyseKLine
#dd = DIFNewHighLogic()
api = TdxHq_API(auto_retry=True)
if api.connect('119.147.212.81', 7709):
    data = api.to_df(api.get_index_bars(9, 1, '000905', 0, 500))  # 返回DataFrame
    start = datetime.datetime.now()
    ak = AnalyseKLine()
    ak.concatKLine(data)
    end = datetime.datetime.now()
    print(end - start)
    print("*" * 50)
    events = ak.getEvents()
    for key in events.keys():
        eventLst = events[key]
        for event in eventLst:
            if event.getEventType() == EventType.HIGHEST_20:
                print("Highest  " + str(key)+" " + str(event.getEIndex()))
    print("*" * 50)
    ak.getKLine().to_csv("e:\\test.xlsx")

    api.disconnect()
quit()
