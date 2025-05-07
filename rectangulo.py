from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def area(self):
        return self._alto * self._ancho