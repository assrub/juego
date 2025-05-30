import pygame
from util import *
from .texto import Texto
from .jugador import Jugador

class Juego(pygame.sprite.Sprite):
    def __init__(self, nivel = 1, jugadores = 1, mejorPuntuacion = 0, enemigos = 0):
        self.nivel = nivel
        self.Cantjugadores = jugadores
        self.mejorPuntuacion = mejorPuntuacion
        self.enemigos = enemigos
        self.jugadorUno = None
        self.naveJugadorUno = None
        self.JugadorDos = None
        self.naveJugadorDos = None
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
            if self.Cantjugadores == 1:
                self.JugadorUno = Jugador()
                self.naveJugadorUno = self.JugadorUno.crearNave()
            elif self.Cantjugadores == 2:
                self.JugadorDos = Jugador()
                self.naveJugadorDos = self.JugadorDos.crearNave()

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
        
        #Aguante el operador TERNARIO!
        naveJugador = self.naveJugadorUno if self.naveJugadorUno else self.naveJugadorDos

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and naveJugador.rect.left > 0:
            naveJugador.moverIzquierda()
        if keys[pygame.K_RIGHT] and naveJugador.rect.right < TAM_PANTALLA_X:
            naveJugador.moverDerecha()
        if keys[pygame.K_UP] and naveJugador.rect.left > 0:
            pass #ARRIBA
        if keys[pygame.K_DOWN] and naveJugador.rect.left < TAM_PANTALLA_Y:
            pass #ABAJO
        if keys[pygame.K_SPACE]:
            naveJugador.Disparar() # IMPLEMENTARRRRRRR

        todos = pygame.sprite.Group()
        todos.add(naveJugador)
        todos.draw(self.pantalla)
        naveJugador.dibujarBala(self.pantalla)

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
