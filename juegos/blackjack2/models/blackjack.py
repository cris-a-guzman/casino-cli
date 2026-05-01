from models.jugador import Jugador
from models.dealer import Dealer
from models.baraja import Baraja

class Blackjack:

    def __init__(self):
        self.jugador = Jugador("player", 5000) #! Esto va en su propio input funcion
        self.dealer = Dealer()

    def pedir_apuesta(self):
        while True:
            monto = input('Ingresa tu apuesta: ')
            if monto.isdigit():
                monto = int(monto)
                if self.jugador.apostar(monto):
                    break
            else:
                print('Lo ingresado no es un numero')

    def repartir_inicial(self):
        for _ in range(2):
            self.jugador.tomar_carta(self.baraja.dar_carta())
            self.dealer.tomar_carta(self.baraja.dar_carta())

        print(self.jugador.mostrar_mano())
        print(self.dealer.mostrar_primera_oculta())

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
        self.baraja = Baraja()
        self.pedir_apuesta()
        self.repartir_inicial()
        self.turno_jugador()
        # self.dealer.mostrar_carta_oculta()
        # self.turno_dealer()
        # self.verificar_ganador()
        # self.pagar_apuesta()



        