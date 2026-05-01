class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.cartas = []

    def tomar_carta(self,carta):
        self.cartas.append(carta)

    def sumar_puntos(self):
        pass

    def mostrar_mano(self):
        pass

    def tiene_blackjack(self):
        pass

    def se_paso(self):
        pass