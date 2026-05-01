import random

def tirar_carta(mazo):
    carta = mazo.pop(random.randrange(len(mazo)))
    print(f"Salio el {carta}")
    return carta

def verificar_blackjack(jugador, dealer):
    if jugador.puntaje == 21:
        print('ganaste')
    elif dealer.puntaje == 21:
        print('gano el dealer')
    #! Aca va el ganador

def jugar_blackjack(mazo, jugador, dealer):
    # saldo = 1000

    turno = 1
    print('Empezando blackjack')

    for i in range(2):
        print(f'Turno {turno}')
        carta = tirar_carta(mazo)
        jugador.agregar_carta(carta)
        jugador.sumar_puntaje(carta.valor)

        carta = tirar_carta(mazo)
        dealer.agregar_carta(carta)
        dealer.sumar_puntaje(carta.valor)
        turno += 1

    print(dealer)
    print(jugador)
    verificar_blackjack(jugador,dealer)


