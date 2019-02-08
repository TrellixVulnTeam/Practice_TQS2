from Inheritance import BinaryGate

class AndGate(BinaryGate.BinaryGate):

    def __init__(self, n):
        BinaryGate.BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 1
        else:
            return 0


gate1 = AndGate("And_Gate_1")
print(gate1.getOutput())
