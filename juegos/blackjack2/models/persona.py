from models.mano import Mano
class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.mano = Mano()

    def tomar_carta(self,carta):
        self.mano.tomar_carta(carta)

    def sumar_puntos(self):
        total = self.mano.sumar_puntos()
        return total

    def mostrar_mano(self):
        mensaje = self.mano.mostrar()
        return mensaje

    def tiene_blackjack(self):
        pass

    def se_paso(self):
        pass