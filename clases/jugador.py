class Jugador():
    def __init__ (self, puntuaciónObtenida = 0, cantVidas = 3, cantBanderas = 0):
        super().__init__()
        self.puntuaciónObtenida = puntuaciónObtenida
        self.cantVidas = cantVidas
        self.cantBanderas = cantBanderas 