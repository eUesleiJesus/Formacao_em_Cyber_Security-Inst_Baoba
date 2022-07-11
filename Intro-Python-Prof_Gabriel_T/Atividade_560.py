'''
Faça uma classe carro com:
atribytos: marva, ano e preço
métodos: mostrar_preço e mostrar_informacoes(motrar todos os atributos do carro
'''


class Carro():
    def __init__(self, marca, ano, preco):
        self.__marca = marca
        self.__ano = ano
        self.__preco = preco

    def mostrar_preco(self):
       print(f' R$ {self.__preco}')

    def mostrar_informacoes(self):
        print(f'{self.__marca} - {self.__ano}')

Gol = Carro("Gol", 82, 45.24161)

Carro.mostrar_preco(Gol)
Carro.mostrar_informacoes(Gol)