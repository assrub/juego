from .nave import Nave

class Enemigo (Nave):
    def __init__(self, color, ubicacionIniciaX, ubicacionIniciaY, velocidad, imagen, tamEnemigoSpriteX=50, tamEnemigoSpriteY=50):
        super().__init__(color, ubicacionIniciaX, ubicacionIniciaY, velocidad, imagen, tamEnemigoSpriteX, tamEnemigoSpriteY)
        self.cord_x = ubicacionIniciaX
        self.cord_y = ubicacionIniciaY
        self.velocidad = velocidad
        self.imagen = imagen

    
    def ataqueENPicada(self):
        pass  # Implementar lógica de ataque en picada

    def update(self):
        pass  # Implementar lógica de actualización del enemigo