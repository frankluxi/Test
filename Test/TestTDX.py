from pytdx.hq import TdxHq_API

api = TdxHq_API(auto_retry=True)
if api.connect('119.147.212.81', 7709):
    data = api.to_df(api.get_index_bars(9, 1, '000905', 0, 500))  # 返回DataFrame
    print(data)
    print(data.high.values)
    api.disconnect()
quit()