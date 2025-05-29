import pygame
from .texto import Texto

class Juego(pygame.sprite.Sprite):
    def __init__(self, nivel = 1, jugadores = 1, mejorPuntuacion = 0, enemigos = 0):
        self.nivel = nivel
        self.mejorPuntuacion = mejorPuntuacion
        self.enemigos = enemigos
        self.fondo = None
        self.finalizarJuego = False
        self.teclasPresionadas = None
        self.jugadores = jugadores
        self.juegoMostrarMenu = True

    def mostrarMenu(self, pantalla, fondo, tamPantallaX, tamPantallaY):
        self.fondo = fondo
        if self.teclasPresionadas == pygame.K_UP:
            if self.jugadores == 1:
                self.jugadores = 2
            else:
                self.jugadores = 1
            self.teclasPresionadas = None 

        if self.teclasPresionadas == pygame.K_DOWN:
            if self.jugadores == 2:
                self.jugadores = 1
            else:
                self.jugadores = 2
            self.teclasPresionadas = None

        if self.teclasPresionadas == pygame.K_RETURN:
            self.juegoMostrarMenu = False
            

        pantalla.blit(fondo, (0, 0))

        txtPlayer1 = Texto(pantalla, "Player 1", pygame.font.Font(None, 48), (255, 255, 0) if self.jugadores == 1 else (255, 255, 255), (tamPantallaX*0.4,tamPantallaY*0.4))   
        txtPlayer1.renderizar()
        txtPlayer2 = Texto(pantalla, "Player 2", pygame.font.Font(None, 48), (255, 255, 0) if self.jugadores == 2 else (255, 255, 255), (tamPantallaX*0.4,tamPantallaY*0.5))
        txtPlayer2.renderizar()
        return True


    def iniciarJuego(self, pantalla):
        pantalla.blit(self.fondo, (0, 0))
        print("iniciando el juego")

        

    def finalizarJuego(self):
        pass

    def actualizarJuego(self):
        pass

    def gestionarIteraciones(self):
        pass
    
    def setJugadores(self, jugadores):
        self.jugadores = jugadores
        print("Soy un juego con " + str(self.jugadores))

    def setFinalizarJuego(self, finalizarJuego):
        self.finalizarJuego = finalizarJuego 

    def getFinalizarJuego(self):
        return self.finalizarJuego
    
    def keyPressed(self, tecla):
        self.teclasPresionadas = tecla

    def getMostrarMenu(self):
        return self.juegoMostrarMenu