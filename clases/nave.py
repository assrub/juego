import pygame
class Nave (pygame.sprite.Sprite):
    def __init__ (self, ubicacionIniciaX, ubicacionIniciaY, velocidad, imagen, tamNaveJugadorX=50, tamNaveJugadorY=50):
        super().__init__()
        self.tamNaveJugadorX = tamNaveJugadorX
        self.tamNaveJugadorY = tamNaveJugadorY
        self.cord_x = ubicacionIniciaX
        self.cord_y = ubicacionIniciaY
        self.velocidad = velocidad
        self.imagen = imagen 
        self.img = pygame.image.load(self.imagen).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.tamNaveJugadorX, self.tamNaveJugadorY))
        self.image = self.img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.cord_x, self.cord_y))
    
    def moverIzquierda(self):
        self.rect.x -= self.velocidad 

    def moverDerecha(self):
        self.rect.x += self.velocidad 

    def Disparar(self):
        pass

    def update(self):  
        pass  # Implementar lógica de actualización de la nave, si es necesario