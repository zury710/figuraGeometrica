from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)
        self._lado = lado

    def area(self):
        return self._lado * self._lado

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, lado):
        self._lado = lado
        super().__init__(lado, lado)