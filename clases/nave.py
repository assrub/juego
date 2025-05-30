import pygame
class Nave (pygame.sprite.Sprite):
    def __init__ (self, color, ubicacionIniciaX, ubicacionIniciaY, velocidad, imagen, tamJugadorSpriteX=50, tamJugadorSpriteY=50):
        self.color = color
        self.cord_x = ubicacionIniciaX
        self.cord_y = ubicacionIniciaY
        self.velocidad = velocidad
        self.imagen = imagen
        
        self.img = pygame.image.load(imagen).convert_alpha()
        self.img = pygame.transform.scale(self.img, (tamJugadorSpriteX, tamJugadorSpriteY))
        self.image = self.img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.cord_x, self.cord_y))
    
    def moverIzquierda(self):
        self.cord_x -= self.velocidad
        self.rect.x = self.cord_x

    def moverDerecha(self):
        self.cord_x += self.velocidad
        self.rect.x = self.cord_x

    def Disparar(self):
        pass

    def update(self):  
        pass  # Implementar lógica de actualización de la nave, si es necesario