
class Mano:
    def __init__(self) -> None:
        self.cartas = []
    
    def tomar_carta(self,carta):
        self.cartas.append(carta)

    def limpiar_mano(self):
        self.cartas = []
    
    def sumar_puntos(self):
        puntos = 0
        for i in self.cartas:
            puntos += i.valor
        return puntos

    def mostrar(self):
        cartas = ", ".join(carta.__str__() for carta in self.cartas)
        puntaje = self.sumar_puntos()
        return f"Puntaje: {puntaje} | Cartas: '{cartas}'"
