from Inheritance import UnaryGate

class NotGate(UnaryGate.UnaryGate):

    def __init__(self, n):
        UnaryGate.UnaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        elif a == 0:
            return 1

gate2 = NotGate("Gate2")
print(gate2.getOutput())