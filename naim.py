from src.circunferencia import cuadrado
from src.color import Color
from src.cuadrado import Cuadrado
from src.rectangulo import rectangulo

c1= cuadrado(lado=6, color= "Rojo")
c2= cuadrado(lado=7, color= "Amarillo")
c3= cuadrado(lado=8, color= "Blanco")
c4= cuadrado(lado=9, color= "Verde")
c5= cuadrado(lado=4, color= "Negro")
r1= rectangulo(lado=8, ancho=7, color= "Negro")
r2= rectangulo(lado=2, ancho=6, color= "Verde")
r3= rectangulo(lado=1, ancho=6, color= "Blanco")
r4= rectangulo(lado=4, ancho=5, color= "Rojo")
r5= rectangulo(lado=7, ancho=9, color= "Amarillo")
circ = circunferencia(radio=9, color='Rojo')


def calcular_dimensiones(lista):
    for fg in lista:
        if isinstance(fg, rectangulo):
            print('rectangulo')
        elif isinstance(fg, cuadrado):
            print('cuadrado')
        print(fg)
        print(f'Area: {fg.area()}')
        print(f'Perimetro: {fg.perimetro()}')
        print('*'. center (50,'*'))



lista_fg = [c1, r1, c2, c3, c4, c5,r2, r3, r4, r5, circ]
calcular_dimensiones(lista_fg)