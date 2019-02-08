from Inheritance import LogicGate

class UnaryGate(LogicGate.LogicGate):

    def __init__(self, n):
        LogicGate.LogicGate.__init__(self, n)
        # super(UnaryGate,self).__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Enter pin input for gate " + self.getLabel() + "=>"))

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error no empty pins")