from Rule.Rule import Rule


class FirstRule(Rule):

    def __init__(self):
        self._strategyCode = "0001"
        self._strategyName = "第一个策略"

    def subStrategy1(self):
        # 20日以上均线短期均线大于长期均线
        if self._data is None:
            print("基础数据无效")
            return False
        row = self._data.shape[0] - 1;
        ma20 = self._data.loc[row, 'MA20']
        ma30 = self._data.loc[row, 'MA30']
        ma60 = self._data.loc[row, 'MA60']
        ma120 = self._data.loc[row, 'MA120']
        ma250 = self._data.loc[row, 'MA250']
        return True if ma20 > ma30 > ma60 > ma60 > ma120 > ma250 else False

    def subStrategy2(self):
        row = self._data.shape[0] - 1
        ret = True
        for num in range(30):
            ma20 = self._data.loc[row - num, 'MA20']
            ma30 = self._data.loc[row - num, 'MA30']
            if ma20 <= ma30:
                ret = False
                break
        return ret

    def subStrategy3(self):
        row = self._data.shape[0] - 1
        ret = True
        for num in range(7):
            close = self._data.loc[row - num, 'close']
            max20 = self._data.loc[row - num - 1, 'MAX20']
            if close <= max20:
                ret = False
                break
        return ret

    def subStrategy4(self):
        row = self._data.shape[0] - 1
        dif = self._data.loc[row, 'DIF']
        dea = self._data.loc[row, 'DEA']
        if dif >= dea:
            return False
        greenCout = 0;
        ret = True
        for num in range(30):
            dif = self._data.loc[row - num, 'DIF']
            dea = self._data.loc[row - num, 'DEA']
            if dif >= dea:
                ret = False
                break
            else:
                greenCout += 1
        return True if greenCout < 30 else False

    def runRule(self):
        return True if self.subStrategy1() and self.subStrategy2() and self.subStrategy3() and self.subStrategy4() else False
