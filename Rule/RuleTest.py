import OldLogic.LogicTest as logics
from OldLogic.MACDHigh import MACDHigh
from Rule.Rule import Rule


class TestRule(Rule):

    def __init__(self):
        logic1 = logics.Logic1()
        logic2 = logics.Logic2()
        macdHigh = MACDHigh()

        self.addLogic(logic1)
        self.addLogic(logic2)
        self.addLogic(macdHigh)