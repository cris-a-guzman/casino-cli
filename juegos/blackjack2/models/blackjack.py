from models.jugador import Jugador
from models.dealer import Dealer
from models.baraja import Baraja

class Blackjack:

    def __init__(self):

        self.baraja = Baraja()
        self.jugador = Jugador("player", 5000)
        self.dealer = Dealer()

    def pedir_apuesta(self):
        apuesta = int(input('ingresa tu apuesta: '))
        if self.jugador.saldo < apuesta:
            print('No tenes esa cantidad para apostar.')

    def repartir_inicial(self):
        pass

    def turno_jugador(self):
        pass

    def turno_dealer(self):
        pass

    def verificar_ganador(self):
        pass

    def pagar_apuesta(self):
        pass

    def reiniciar_ronda(self):
        pass

    def iniciar_juego(self):
        self.baraja.crear_mazo()
        self.baraja.mezclar()
        pass