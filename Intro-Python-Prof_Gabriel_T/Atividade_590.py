"""
crie uma classe chamada circulo que tenha um raio privado e as seguintes funções:
mudar raio
retornar raio
cálculo e retorno do diâmetro
cálculo e retorno da circunferência
"""

import math

class Circulo():
    def __init__(self, raio):
        self.__raio = raio

    def mudar_raio(self, raio):
        self.__raio = raio
    def retornar_raio(self):
        return self.__raio

    def diametro(self):
        return 2 * self.__raio
    def circunferencia(self):
        return 2 * math.pi * self.__raio

"""
Crie uma classe chamada retangulo que possua um ladoA e um ladoB (horizontal e vertical respectivamente
ambros privados
A classe retangulo deve possuir as seguintes funções:
1. uma função para mudar e outra para retornar cada lado (A&B)
2 cálculo da área
3 cálculo do perímetro"""

"""
class Retangulo():
    def __init__(self, ladoA, ladoB):
        self.__ladoA = ladoA
        self.__ladoB = ladoB

    def mudar_ladoA(self, ladoA):
        self.__ladoA = ladoA

    def mudar_ladoB(self, ladoB):
        self.__ladoB = ladoB

    def retornar_ladoA(self):
        return self.__ladoA

    def retornar_ladoB(self):
        return self.__ladoB

    def area(self):
        return self.__ladoA * self.__ladoB

    def perimetro(self):
        return (2 * self.__ladoA) + (self.__ladoB * 2)
"""
"""
quad = Retangulo(4, 5)

print(Retangulo.area(quad))
print(Retangulo.perimetro(quad))
print(Retangulo.retornar_ladoA(quad))
Retangulo.mudar_ladoA(quad, 6)
print(Retangulo.retornar_ladoA(quad))
print(Retangulo.area(quad))
print(Retangulo.perimetro(quad))
print(Retangulo.retornar_ladoA(quad))
"""


class Retangulo():
    def __init__(self, ladoA, ladoB):
        self.__ladoA = ladoA    #Horizontal
        self.__ladoB = ladoB    #Vertical

    def mudar_ladoA(self, ladoA):
        self.__ladoA = ladoA
    def mudar_ladoB(self, ladoB):
        self.__ladoB = ladoB
    def retornar_ladoA(self):
        return self.__ladoA
    def retornar_ladoB(self):
        return self.__ladoB

    def area(self):
        return self.__ladoA * self.__ladoB
    def perimetro(self):
        return 2 * (self.__ladoA + self.__ladoB)

""" 
crie uma função chamada quantos_circulos que receba  um círculo e um retângulo e calcule quantos cícurlos cabem em um retânculo
"""

"""
def quantos_circulos(circulo, retangulo):
    areaRet = Retangulo.area(retangulo)
    areaCir = Circulo.circunferencia(circulo)
    return areaRet / areaCir

quad = Retangulo(90, 50)
cir = Circulo(5)

print(quantos_circulos(cir, quad))
"""
def quantos_circulos(retangulo, circulo):
    qtd_horizontal = 0
    qtd_vertical = 0

    ladoA = retangulo.retornar_ladoA()
    ladoB = retangulo.retornar_ladoB()

    #Horizontal
    while(circulo.diametro() * (qtd_horizontal + 1) <= ladoA):
        qtd_horizontal += 1;

    #Vertical
    while(circulo.diametro() * (qtd_vertical + 1) <= ladoB):
        qtd_vertical += 1;

    total = qtd_horizontal * qtd_vertical
    resultado = (qtd_horizontal, qtd_vertical, total)

    return resultado

circ = Circulo(5)
rect = Retangulo(300, 300  )

resultado = quantos_circulos(rect, circ)
print(f'Hor.: {resultado[0]}, Ver.: {resultado[1]}, Total: {resultado[2]}')
