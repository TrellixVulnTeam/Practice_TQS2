from Inheritance import BinaryGate

class OrGate(BinaryGate.BinaryGate):

    def __init__(self, n):
        BinaryGate.BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0