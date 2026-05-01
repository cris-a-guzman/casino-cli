import random
class Carta:
    def __init__(self, palo, valor, nombre) -> None:
        self.palo = palo
        self.valor = valor
        self.nombre = nombre

    def __getitem__(self, key):
        if key == "palo":
            return f'El palo de la carta es: {self.palo}'
        if key == "valor":
            return f'El valor de la carta es: {self.valor}'
        else:
            return 'Algo salio mal'

    def __str__(self) -> str:
        return f'{self.nombre} de {self.palo}'

class Baraja:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.lista_cartas = [[],[],[],[]]
        self.palos = ["♠", "♥", "♦", "♣"]
        self.mazo = []

    def agregar_carta(self,carta,palo):
        self.lista_cartas[palo].append(carta)

    def mezclar(self):
        for i in self.lista_cartas:
            for j in i:
                self.mazo.append(j)
        random.shuffle(self.mazo)
        return self.mazo
    
    def __getitem__(self, palo):
        return self.lista_cartas[palo]

    def __str__(self) -> str:
        resultado = []

        for i, cartas in enumerate(self.lista_cartas):
            resultado.append(f"\nPalo: {self.palos[i]}")

            for k in range(0, len(cartas), 3):
                grupo = cartas[k:k+3]
                linea = " | ".join(f"* {c}" for c in grupo)
                resultado.append(linea)

        return "\n".join(resultado)
 
class Jugador:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.cartas = []
        self.puntaje = 0

    def agregar_carta(self,carta):
        self.cartas.append(carta)
    
    def sumar_puntaje(self, puntaje):
        self.puntaje += puntaje


    def __str__(self) -> str:
        cartas = ", ".join(c.nombre.title() for c in self.cartas)
        return f"Puntaje de {self.nombre.title()} = {self.puntaje} | Cartas: {cartas}"

    