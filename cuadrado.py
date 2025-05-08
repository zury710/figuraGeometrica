from color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, color):
    def __init__(self, lado=0, color=None):
       figurageometrica.__init__(self, ancho=lado, alto=lado)
        color.__init__(self, nombre=color)

    def area(self):
        return self._lado * self._lado

    def __str__(self):
        return f"cuadrado: {self,__dict__.__str__()}
if __name__ == '__main__':
    c1 = cuadrado(lado=6, color=Color('red'))