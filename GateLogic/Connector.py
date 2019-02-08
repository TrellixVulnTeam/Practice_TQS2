from Inheritance import AndGate, NotGate, OrGate

class Connector:

    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate

        self.to_gate = to_gate

        to_gate.setNextPin(self)

        def getFrom(self):
            return self.from_gate

        def getTo(self):
            return self.to_gate


g1 = AndGate.AndGate("G1")
g2 = AndGate.AndGate("G2")
g3 = OrGate.OrGate("G3")
g4 = NotGate.NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
print("OUTPUT:", g4.getOutput())