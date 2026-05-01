from clases import Carta, Baraja, Jugador
from cartas import crear_cartas, mezclar
from menu import menu
from logica import jugar_blackjack
import random

dealer = Jugador("Dealer")
player = Jugador("Jugador")

baraja, palos = crear_cartas()

def jugar():
    while True:
        menu()
        user_choice = input(' Ingresa el numero de la opcion: ').strip()
        if user_choice == "1":
            print(baraja)
        elif user_choice == "2":
            palo = random.randint(0,3)
            numero = random.randint(0,11)
            carta = baraja[palo]
            print(carta[numero])
        elif user_choice =="3":
            mazo = baraja.mezclar()
            # jugar_blackjack(mazo)
            # calcular_puntaje(baraja)
        elif user_choice == "4":
            print('Bye...')
            break
        else:
            print(' Lo ingresado no corresponde a una opcion, intentelo de nuevo.')

mazo = baraja.mezclar()
jugar_blackjack(mazo,player,dealer)