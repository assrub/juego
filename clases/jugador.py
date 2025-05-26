import pygame

class jugador (pygame.spirte.pygame.sprite.Sprite):
    def _init_ (self, x, y, velocidad, life = 3):
        super()._init_()
        self.img = pygame.image.load().convert_alpha
        self.img = pygame.transform.scale(self.img, ())
        self.puntuacionObtenida = 0
        self.life = life