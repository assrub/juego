import pygame
from clases import *
#INSTANCIAS
pygame.init()

reloj = pygame.time.Clock()

juego = Juego() 
 
while not juego.finalizarJuego: 
    reloj.tick(30) # Limita a 30 FPS
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego.setFinalizarJuego(True)
            
        if evento.type == pygame.KEYDOWN:
            juego.keyPressed(evento.key)
                
    if juego.mostrarMenu():
        pass
    else:
        juego.iniciarJuego()
        
    pygame.display.update()
    
