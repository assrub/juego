import pygame
class Bala (pygame.sprite.Sprite):
    def __init__(self, tipoDeBala, ubicacionIniciaX, ubicacionIniciaY, velocidad, image):
        super().__init__()
        self.tipoDeBala = tipoDeBala
        self.cord_x = ubicacionIniciaX 
        self.cord_y = ubicacionIniciaY
        self.velocidad = velocidad
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect(topleft=(self.cord_x, self.cord_y))
        self.mask = pygame.mask.from_surface(self.image)


        def disparar(self):
            pass  # Implementar lógica de disparo de la bala

        def update(self):
            pass  # Implementar lógica de actualización de la bala