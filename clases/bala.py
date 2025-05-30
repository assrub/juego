import pygame
from util import *

class Bala(pygame.sprite.Sprite): 
    def __init__(self, x, y, velocidad):
        super().__init__()
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.tam_bala = TAM_SPRITE_BALA

        # Crea una superficie (imagen) cuadrada donde se va a dibujar la bala (El tamaño es doble del radio para que el circulo entre completo).
        self.image = pygame.Surface((self.tam_bala*2, self.tam_bala*2), pygame.SRCALPHA) 
        # Dibuja la bala como un círculo rojo, sus argumentos son:
        # 1 - La superficie donde se dibuja.
        # 2 - El color (rojo).
        # 3 - La posición (x, y) de la bala.
        # 4 - El radio del círculo (5) que equivale a 5 píxeles.
        #pygame.draw.circle(pantalla, (255, 0, 0), (int(self.x), int(self.y)), self.tam_bala)
        pygame.draw.circle(self.image, COLOR_SPRITE_BALA, (self.tam_bala, self.tam_bala), self.tam_bala)
        # Crea un rectángulo (rect) que representa la posición y el tamaño de la bala, el centro del rectángulo es (x, y).
        self.rect = self.image.get_rect(center=(self.x, self.y))
        #Crea una máscara para detectar colisiones "pixel-perfect" (solo en donde hay color, no en el fondo transparente).
        self.mask = pygame.mask.from_surface(self.image)
       
    def mover(self):
        self.y -= self.velocidad
        self.rect.center = (self.x, self.y)

    def dibujar(self, pantalla):
        #Blit es un método fundamental de Pygame que dibuja una superficie (Surface) sobre otra.
        pantalla.blit(self.image, self.rect)

    def getPosicion_x(self):
        return self.x
    
    def getPosicion_y(self):
        return self.y