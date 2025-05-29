import pygame
from .bala import Bala
from util import TAM_JUGADOR_SPRITE_X, TAM_JUGADOR_SPRITE_Y, VELOCIDAD_SPRITE_BALA


class jugador (pygame.spirte.pygame.sprite.Sprite):
    def _init_ (self, x, y, velocidad, life = 3):
        super()._init_()
        self.img = pygame.image.load("./assets/Imagenes/nave jugador.jpg").convert_alpha
        self.img = pygame.transform.scale(self.img, (TAM_JUGADOR_SPRITE_X, TAM_JUGADOR_SPRITE_Y))
        self.image = self.img
        self.mask = pygame.mask.from_surface(self.image)
        self.puntuacionObtenida = 0
        self.life = life
        self.direccion = 'izq, der, arr, abj'
        self.velocidad = velocidad
        self.rect = self.image.get_rect(topleft=(x,y))
        self.balaDisparadas = pygame.sprite.Group()
        self.colisionandoAntes = False
        
    def mover(self, direccion):
        if direccion == 'izq':
            self.rect.x -= self.velocidad
            angulo = 90
        elif direccion == 'der':
            self.rect.x += self.velocidad
            angulo = -90
        elif direccion == 'arr':
            self.rect.y -= self.velocidad
            angulo = 0
        elif direccion == 'abj':
            self.rect.y += self.velocidad
            angulo = 180
            
        self.direccion = direccion
        self.image = pygame.transform.rotate(self.img, angulo)
        self.mask = pygame.mask.from_surface(self.image)
    
    def disparar (self):
        nuevaBala = Bala(self.rect.centerx, self.rect.centery, VELOCIDAD_SPRITE_BALA, self.direccion)
        self.balaDisparadas.add(nuevaBala)
        
    def dibujarBala(self, pantalla):
        for bala in self.balaDisparadas:
            bala.mover()
            bala.dibujar(pantalla)
            if bala.getPosicion_x() <= 0 or bala.getPosicion_x() >= pantalla.get_width() or bala.getPosicion_y() <= 0 or bala.getPosicion_y() >= pantalla.get_height():
               bala.kill()

    def meColisionaron(self, personaje):
        colisionandoAhora = pygame.sprite.spritecollide(self, personaje, False, pygame.sprite.collide_mask)
        if colisionandoAhora and not self.colisionandoAntes:
           self.colisionandoAntes = True
           self.descontarVida()
           if self.life == 0:
               self.kill() 
        elif not colisionandoAhora:
            self.colisionandoAntes = False
           
    def balasDisparadas(self):     
        return self.balaDisparadas
    
    def incrementarPuntaje(self):
        self.puntaje += 1
    
    def descontarVida(self):
        if self.life > 0: 
            self.life -= 1

    def jugadorVerVida(self):
        return self.life

    def descontarVida(self):
        if self.life > 0:
            self.life -= 1 