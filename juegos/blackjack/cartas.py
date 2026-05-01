from clases import Baraja, Carta
def crear_cartas():
    baraja = Baraja("baraja de cartas")
    palos = ["♠", "♥", "♦", "♣"]

    for i,palo in enumerate(palos):
        for valor in range(1,14):
            if valor == 1:
                carta = Carta(palo,11,"As")
            elif valor >= 11:
                carta = Carta(palo, 10,["J","Q","K"][valor-11])
            else:
                carta = Carta(palo,valor,str(valor))
            baraja.agregar_carta(carta,i)
    return baraja, palos

def mezclar(baraja):
    baraja.mezclar()
    