"""
classe conta corrente: crie uma classe para implementar uma conta corrente.
a classe deve possuir os seguintes atributos
númedo da conta
nome do correntista
saldo

os mérodos são os seguintes
alterarNome
depósito
saque

no contrsuto, saldo é opcional, com valor default zero e os demais atributos são obrigatórios

class text():
    def__init__(self, numero = 0, nome): default
"""
class conta_corrente():
    def __init__(self, numero, nome, saldo = 0):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo

    def alterarNome(self, nome):
        self.__nome = nome

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if(self.__saldo > 0 and (self.__saldo - valor) >= 0):
            self.__saldo -= valor
            return
        print(f'Nao ha saldo o suficiente para sacar R$ {valor}.')

conta = conta_corrente(1648864, "Teste Silva")
conta.deposito(10000)
conta.saque(500)
