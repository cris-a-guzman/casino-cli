class Apuesta:
    def __init__(self,  monto):
        self.monto = monto

    def pagar(self):
        return self.monto*2

    def perdio(self):
        return 0