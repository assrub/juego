
class Texto():
    def __init__(self, objeto, texto, fuente, color, ubicacion=(10, 10)):
        self.objeto = objeto
        self.texto = texto
        self.fuente = fuente
        self.ubicacion = ubicacion
        self.color = color

    def renderizar(self):
        txt = self.fuente.render(self.texto, True, self.color) 
        self.objeto.blit(txt, self.ubicacion)

 