from models.persona import Persona

class Jugador(Persona):

    def __init__(self, nombre, saldo):
        super().__init__(nombre)

        self.saldo = saldo
        self.apuesta = 0

    def apostar(self):
        pass
    
    def pedir(self):
        pass

    def quedarse(self):
        pass

    def duplicar(self):
        pass

    def dividir(self):
        pass

