from pytdx.hq import TdxHq_API
import pandas as pd

api = TdxHq_API(auto_retry=True)
if api.connect('119.147.212.81', 7709):
    data = api.to_df(api.get_index_bars(9, 1, '000905', 1, 500))  # 返回DataFrame




    print(data)
    # print(data.high.values)
    print("*" * 50)

    data1 = api.to_df(api.get_index_bars(9, 1, '000905', 0, 1))# 返回DataFrame
    print(type(data1))
    data = pd.concat([data,data1],axis=0,ignore_index=True)
    # data.append(data1,ignore_index=True)

    print(data)
    api.disconnect()
quit()
