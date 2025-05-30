import pygame
from util import *
from .texto import Texto

class Juego(pygame.sprite.Sprite):
    def __init__(self, nivel = 1, jugadores = 1, mejorPuntuacion = 0, enemigos = 0):
        self.nivel = nivel
        self.Cantjugadores = jugadores
        self.mejorPuntuacion = mejorPuntuacion
        self.enemigos = enemigos

        self.tamañoPantallaX = TAM_PANTALLA_X
        self.tamañoPantallaY = TAM_PANTALLA_Y
        self.showMenu = True
        self.finalizarJuego = False
        self.teclasPresionadas = None

        #VARIABLES
        self.pantalla = pygame.display.set_mode((self.tamañoPantallaX, self.tamañoPantallaY))
        self.fondo = pygame.image.load(SRPITE_FONDO_PANTALLA).convert()
        self.fondo = pygame.transform.scale(self.fondo, (self.tamañoPantallaX, self.tamañoPantallaY))
        pygame.display.set_caption("GALAXIAN")


    def mostrarMenu(self): 
        if self.teclasPresionadas == pygame.K_UP:
            if self.Cantjugadores == 1:
                self.Cantjugadores = 2
            else:
                self.Cantjugadores = 1
            self.teclasPresionadas = None 

        if self.teclasPresionadas == pygame.K_DOWN:
            if self.Cantjugadores == 2:
                self.Cantjugadores = 1
            else:
                self.Cantjugadores = 2
            self.teclasPresionadas = None

        if self.teclasPresionadas == pygame.K_RETURN:
            self.showMenu = False
            

        self.pantalla.blit(self.fondo, (0, 0))

        txtPlayer1 = Texto(self.pantalla, "Player 1", pygame.font.Font(FUENTE_MENU_FONT, FUENTE_MENU_TAMAÑO), 
                           FUENTE_MENU_COLOR_SELECCION if self.Cantjugadores == 1 else FUENTE_MENU_COLOR, 
                           (self.tamañoPantallaX*0.4,self.tamañoPantallaY*0.4))   
        txtPlayer1.renderizar()
        txtPlayer2 = Texto(self.pantalla, "Player 2", pygame.font.Font(FUENTE_MENU_FONT, FUENTE_MENU_TAMAÑO), 
                           FUENTE_MENU_COLOR_SELECCION if self.Cantjugadores == 2 else FUENTE_MENU_COLOR, 
                           (self.tamañoPantallaX*0.4,self.tamañoPantallaY*0.5))
        txtPlayer2.renderizar()


    def iniciarJuego(self):
        self.actualizarJuego() 


    def getShowMenu(self):
        return self.showMenu
    
    def setFinalizarJuego(self, finalizarJuego):
        self.finalizarJuego = finalizarJuego 

    def finalizarJuego(self):
        return self.finalizarJuego

    def actualizarJuego(self):
        self.pantalla.blit(self.fondo, (0, 0))

    def gestionarIteraciones(self):
        pass
    
    def keyPressed(self, tecla):
        self.teclasPresionadas = tecla
