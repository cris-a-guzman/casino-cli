from models.jugador import Jugador
from models.dealer import Dealer
from models.baraja import Baraja
import time

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
        while True:
            accion = input('Pedir carta S/N: ').lower().strip()
            if accion == "s":
                self.jugador.tomar_carta(self.baraja.dar_carta())

                if self.jugador.se_paso():
                    print(self.jugador.mostrar_mano())
                    print('Te pasaste.')
                    break
                else:
                    print(self.jugador.mostrar_mano())
            else:
                break

    def turno_dealer(self):

        print(self.dealer.mostrar_mano())
        while self.dealer.debe_pedir():
            time.sleep(1.5)
            self.dealer.tomar_carta(self.baraja.dar_carta())
            print(self.dealer.mostrar_mano())
            if self.dealer.se_paso():
                print('El dealer se paso de 21')


    def verificar_ganador(self):
        if self.jugador.tiene_blackjack():
            return 'El jugador tuvo blackjack'
        if self.dealer.tiene_blackjack():
            return 'El Dealer tuvo blackjack'
        jugador = self.jugador.sumar_puntos()
        dealer = self.dealer.sumar_puntos()
        if self.jugador.se_paso():
            return 'Gana el Dealer'
        if self.dealer.se_paso():
            return 'Gana el Jugador'
        if jugador > dealer:
            return 'Gana el Jugador'
        elif dealer > jugador:
            return 'Gana el Dealer'
        else:
            return 'Empate'

    def pagar_apuesta(self):
        pass

    def reiniciar_ronda(self):
        pass

    def iniciar_juego(self):
        self.baraja = Baraja()
        self.pedir_apuesta()
        self.repartir_inicial()
        self.turno_jugador()
        self.turno_dealer()
        print(self.verificar_ganador())
        # self.pagar_apuesta()



        