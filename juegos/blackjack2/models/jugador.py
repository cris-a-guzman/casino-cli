from models.persona import Persona
from models.apuesta import Apuesta
class Jugador(Persona): #! Cuando se inicializa Jugador, se declara Saldo en numeros

    def __init__(self, nombre, saldo):
        super().__init__(nombre)
        self.saldo = saldo
        self.apuesta = None

    def apostar(self,monto):
        if monto > self.saldo:
            print('No tenes suficiente saldo.')
            return False
        
        self.apuesta = Apuesta(monto)
        self.saldo -= self.apuesta.monto
        return True
    
    def pedir(self):
        pass

    def quedarse(self):
        pass

    def duplicar(self):
        pass

    def dividir(self):
        pass

