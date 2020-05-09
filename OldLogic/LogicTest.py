from OldLogic.OldLogic import OldLogic


class Logic1(OldLogic):

    def __init__(self):
        self._logicID = "0001"
        self._logicName = "logic1"
    def _doLogic(self):
        return True

    def _doReverseLogic(self):
        return True


class Logic2(OldLogic):
    
    def __init__(self):
        self._logicID = "0002"
        self._logicName = "logic2"

    def _doLogic(self):
        return True

    def _doReverseLogic(self):
        return True