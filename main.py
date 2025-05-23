import pygame
from util import TAM_PANTALLA_X, TAM_PANTALLA_Y

#INSTANCIAS
pygame.init()

#VARIABLES
pantalla = pygame.display.set_mode((TAM_PANTALLA_X, TAM_PANTALLA_Y))
fondo = pygame.image.load("./assets/Imagenes/fondo.jpg").convert()
fondo = pygame.transform.scale(fondo, (TAM_PANTALLA_X, TAM_PANTALLA_Y))
pygame.display.set_caption("J23 - OOP")
reloj = pygame.time.Clock()

corriendo = True
while corriendo: 
    reloj.tick(30) # Limita a 30 FPS
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        next
    if keys[pygame.K_RIGHT]:
        next
    if keys[pygame.K_UP]:
        next
    if keys[pygame.K_DOWN]:
        next
    if keys[pygame.K_SPACE]:
        next
            
    pantalla.blit(fondo, (0, 0))
    pygame.display.update()
    
