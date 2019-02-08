from Inheritance import LogicGate


class BinaryGate(LogicGate.LogicGate):

    def __init__(self, n):
        LogicGate.LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter pin-A input for gate " + self.getLabel() + "=>"))

    def getPinB(self):
        return int(input("Enter pin-B input for gate " + self.getLabel() + "=>"))

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error no empty pins")
