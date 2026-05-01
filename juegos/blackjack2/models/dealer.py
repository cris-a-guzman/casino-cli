from models.persona import Persona

class Dealer(Persona):

    def __init__(self):
        super().__init__("Dealer")

    def jugar_turno(self):
        pass

    def debe_pedir(self):
        pass

    def mostrar_primera_oculta(self):
        puntos = self.mano.cartas[0].valor

        return f"Puntaje Dealer: {puntos} | Cartas: '{self.mano.cartas[0]}, [?]'"

