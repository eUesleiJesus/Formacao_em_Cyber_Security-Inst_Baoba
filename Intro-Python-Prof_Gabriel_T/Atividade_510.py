'''
Atividade 51

Façam uma função que receba o ano de
nascimento do usuário, e retorne sua idade
utilizando datetime.date.today().year.

datetime.date.today().year retorna o ano atual.
'''
import datetime

def idade(ano):
    idade = ano
    idade -= datetime.date.today().year
    return idade * (-1)

ano = 1967

id = idade(ano)

print(id)
'''
import datetime

ano_atual = datetime.date.today().year

def idade(ano_nascimento):
    print(f"Você tem {ano_atual - ano_nascimento} de idade!")

idade(int(input("Digite seu ano de nascimento")))
'''