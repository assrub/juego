import pygame
from util import *
from nave import Nave
from enemigo import Enemigo

class Bala(pygame.sprite.Sprite):
    def __init__(self, dispara: Nave | Enemigo, IMG_BALA, TAMAÑO_BALA, VELOCIDAD_BALA):
        super().__init__()
        self.dispara = dispara

        raw = pygame.image.load(IMG_BALA).convert_alpha()
        self.image = pygame.transform.scale(raw, TAMAÑO_BALA)

        #defino el tipo según quién dispara
        self.tipoDeBala = "jugador" if isinstance(dispara, Nave) else "enemigo"
        self.velocidad = VELOCIDAD_BALA


        self.disparar()


    def disparar(self): #ubica la bala en el cañón del que dispara y ajusta su dirección
        if self.tipoDeBala == "jugador":
            pos = self.dispara.rect.midtop
            self.direccion = -1
        else:
            pos = self.dispara.rect.midbottom
            self.direccion = 1

        #creo o reposiciono el rect según la imagen y la posición calculada
        self.rect = self.image.get_rect(center=pos)


    def update(self): #se mueve y se destruye si sale de pantalla
        self.rect.y += self.velocidad * self.direccion
        alto = pygame.display.get_surface().get_height()
        if self.rect.bottom < 0 or self.rect.top > alto:
            self.kill()


    def getPosicion_x(self):
        return self.x
    
    def getPosicion_y(self):
        return self.y

