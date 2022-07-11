"""Atividade 55
Faça uma calsse pessoa:
Atributos: nome, idade e telefone
Método: mudar_numero(muda o numero de telefone, e envelhecer (aumenta a idade)
"""


class pessoa():
    def __init__(self, nome, idade, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__telefone = telefone

    def mudar_numero(self, telefone):
        self.__telefone = telefone

    def envelhecer(self, idade):
        if idade > self.__idade:
            self.__idade = idade
            return
        print("A idade de entrada deve ser maio que a idade atual.")

pess = pessoa("Teste", 82, 4524161)
pess.mudar_numero(454846472)
pess.envelhecer(91)


"""
class Pessoa:
    def __init__(self, idade, nome, telefone):
        self.idade = idade
        self.nome = nome
        self.telefone = telefone
    def mudar_numero(self, telefone):
        self.telefone = telefone
    def envelhecer(self, idade):
        if idade > self.idade:
            self.idade = idade
            return
        print("A idade de entrade deve ser maior que a idade atual")

pess = Pessoa("Teste", 82, 4524161)
pess.mudar_numero(454846472)
pess.envelhecer(91)
"""

"""
Ueslei = Pessoa()

Ueslei.idade = 30
Ueslei.nome = "Ueslei"
Ueslei.telefone = 71988408516


def __init__(self, mudar_numero, envelhece)

"""