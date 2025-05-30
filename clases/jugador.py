import pygame
from util.constantes import PUNTUACION_INICIAL_JUGADOR, VIDAS_INICIALES_JUGADOR, BANDERAS_INICIALES_JUGADOR

class Jugador:
    def __init__(self, PUNTUACION_INICIAL_JUGADOR, VIDAS_INICIALES_JUGADOR, BANDERAS_INICIALES_JUGADOR):
        
        self.puntuacionObtenida = PUNTUACION_INICIAL_JUGADOR
        self.cantDeVidas = VIDAS_INICIALES_JUGADOR
        self.cantBanderas = BANDERAS_INICIALES_JUGADOR

    def incrementarPuntuacion(self, puntos: int = 1):
        self.puntuacionObtenida += puntos

    def incrementarVidas(self, vidas: int = 1):
        self.cantDeVidas += vidas

    def atrapa(self):
        self.cantBanderas += 1
