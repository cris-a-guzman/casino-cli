from models.carta import Carta
import random

class Baraja:
    def __init__(self) -> None:
        self.mazo = []
        self.palos = ["♠", "♥", "♦", "♣"]

    def crear_mazo(self):
        for i,palo in enumerate(self.palos):
            for valor in range(1,14):
                if valor == 1:
                    carta = Carta(palo,11,"As")
                elif valor >= 11:
                    carta = Carta(palo, 10,["J","Q","K"][valor-11])
                else:
                    carta = Carta(palo,valor,str(valor))
                self.mazo.append(carta)

    def mezclar(self):
        random.shuffle(self.mazo)

    def __str__(self) -> str:
        resultado = []

        for i, cartas in enumerate(self.mazo):
            resultado.append(f"\nPalo: {self.palos[i]}")

            for k in range(0, len(cartas), 3):
                grupo = cartas[k:k+3]
                linea = " | ".join(f"* {c}" for c in grupo)
                resultado.append(linea)

        return "\n".join(resultado)