import pygame
from util import TAM_PANTALLA_X, TAM_PANTALLA_Y
from clases import *
#INSTANCIAS
pygame.init()

#VARIABLES
pantalla = pygame.display.set_mode((TAM_PANTALLA_X, TAM_PANTALLA_Y))
fondo = pygame.image.load("./assets/Imagenes/fondo.jpg").convert()
fondo = pygame.transform.scale(fondo, (TAM_PANTALLA_X, TAM_PANTALLA_Y))
pygame.display.set_caption("J23 - OOP")
reloj = pygame.time.Clock()

juego = Juego() 
 
while not juego.getFinalizarJuego(): 
    reloj.tick(30) # Limita a 30 FPS
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego.setFinalizarJuego(True)
            
        if evento.type == pygame.KEYDOWN:
            juego.keyPressed(evento.key)
                
    if juego.getMostrarMenu():
        iniciarJuego = juego.mostrarMenu(pantalla, fondo, TAM_PANTALLA_X, TAM_PANTALLA_Y)
    if not juego.getMostrarMenu():
        juego.iniciarJuego(pantalla)
        
    pygame.display.update()
    
