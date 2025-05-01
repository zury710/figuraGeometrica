class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def __str__(self):
        return f"Color: {self._color}"

class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def get_alto(self):
        return self._alto

    def set_alto(self, alto):
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    def get_ancho(self):
        return self._ancho

    def set_ancho(self, ancho):
        self._ancho = ancho

    def __str__(self):
        return f"Alto: {self._alto}, Ancho: {self._ancho}"

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado, color=None):
        super().__init__(lado, lado)
        self._lado = lado
        self._color = color

    def area(self):
        return self._lado * self._lado

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, lado):
        self._lado = lado
        super().__init__(lado, lado)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def get_color(self):
        return self._color.color if self._color else None

    def set_color(self, color_obj):
        if isinstance(color_obj, Color):
            self._color = color_obj
        else:
            raise ValueError("Debe proporcionar un objeto de la clase Color.")

    def __str__(self):
        color_str = f", {self._color}" if self._color else ""
        return f"Cuadrado - Lado: {self._lado}, Área: {self.area()}{color_str}"

class Rectangulo(FiguraGeometrica):
    def __init__(self, alto, ancho, color=None):
        super().__init__(alto, ancho)
        self._color = color

    def area(self):
        return self._alto * self._ancho

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def get_color(self):
        return self._color.color if self._color else None

    def set_color(self, color_obj):
        if isinstance(color_obj, Color):
            self._color = color_obj
        else:
            raise ValueError("Debe proporcionar un objeto de la clase Color.")

    def __str__(self):
        color_str = f", {self._color}" if self._color else ""
        return f"Rectángulo - Alto: {self._alto}, Ancho: {self._ancho}, Área: {self.area()}{color_str}"

# Otro ejemplo de uso: creando listas de figuras y calculando áreas
formas = []

formas.append(Cuadrado(10))
formas.append(Rectangulo(5, 8, Color("Verde")))
formas.append(Cuadrado(3, Color("Amarillo")))
formas.append(Rectangulo(7, 2))

for forma in formas:
    print(forma)
    print(f"El área es: {forma.area()}")
    if hasattr(forma, 'get_color') and forma.get_color():
        print(f"El color es: {forma.get_color()}")
    print("-" * 20)