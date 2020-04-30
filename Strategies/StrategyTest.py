from Rule.RuleTest import TestRule
from Strategies.Strategy import Strategy


class TestStrategy(Strategy):
    def __init__(self):
        rule1 = TestRule()
        self.addRule(rule1)
