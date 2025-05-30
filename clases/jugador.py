from util import *
from .nave import Nave
class Jugador:
    def __init__(self):
        self.puntuacionObtenida = PUNTUACION_INICIAL_JUGADOR
        self.cantDeVidas = VIDAS_INICIALES_JUGADOR
        self.cantBanderas = BANDERAS_INICIALES_JUGADOR

    def incrementarPuntuacion(self, puntos: int = 1):
        self.puntuacionObtenida += puntos

    def incrementarVidas(self, vidas: int = 1):
        self.cantDeVidas += vidas

    def atrapa(self):
        self.cantBanderas += 1

    def crearNave(self):
        return Nave((TAM_PANTALLA_X * 0.5), (TAM_PANTALLA_Y - TAM_NAV_JUGADOR_Y - 10), VELOCIDAD_NAV_JUGADOR, IMG_NAVE_JUGADOR, TAM_NAV_JUGADOR_X, TAM_NAV_JUGADOR_Y)
         

