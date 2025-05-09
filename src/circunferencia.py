import math

from src.color import Color
from src.FiguraGeometrica import FiguraGeometrica


class circunferencia(FiguraGeometrica, Color):
    def __init__(self, radio=0, color=None):
        FiguraGeometrica.__init__(self, ancho=radio, alto=0)
        color.__init__(self,nombre=color)

    def __str__(self):
            return f'Circunferencia-> [radio= {self . ancho}´, color {self._color}]'

    def area(self):
            return math.pi * self.ancho * self.ancho

    def perimetro(self):
            return math.pi * 2 * self.ancho

if __name__ == '__main__':
    c1 = circunferencia(color='red' , radio=5)
    print(c1)
    print(f'area = {c1.area()}')
    print(f'perimetro = {c1.perimetro()}')

