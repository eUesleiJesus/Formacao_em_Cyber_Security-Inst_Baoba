"""
um racional e qualquer  número da forma p/q, sendo p inteiro e q inteiro não nulo.
crie uma classe para representar um racional e os seguintes métodos
inverter sinal
somar dois racionais
subtrair dois racionais
produto de dois racionais
quociente de dois racionais
"""

class Racional():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def inverter_sinal(self, r):
        r = Racional(-r.numerador, r.denominador)
        return r

    def somar_racionais(self, r1, r2):
        r = Racional((r1.numerador * r2.denominador) + (r2.numerador * r1.denominador),
        r2.denominador * r1.denominador)
        return r

    def subtrair_racionais(self, r1, r2):
        r = Racional((r1.numerador * r2.denominador) - (r2.numerador * r1.denominador),
		r2.denominador * r1.denominador)
        return r

    def produto_racionais(self, r1, r2):
        r = Racional(r1.numerador * r2.numerador, r1.denominador * r2.denominador)
        return r

    def quociente_racionais(self, r1, r2):
        r = Racional(r1.numerador * r2.denominador, r1.denominador * r2.numerador)
        return r.numerador/r.denominador
