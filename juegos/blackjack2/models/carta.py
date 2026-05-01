class Carta:
    def __init__(self, palo, valor, nombre) -> None:
        self.palo = palo
        self.valor = valor
        self.nombre = nombre

    def __getitem__(self, key): #! Esto no es necesario
        if key == "palo":
            return f'El palo de la carta es: {self.palo}'
        if key == "valor":
            return f'El valor de la carta es: {self.valor}'
        else:
            return 'Algo salio mal'

    def __str__(self) -> str:
        return f'{self.nombre} de {self.palo}'