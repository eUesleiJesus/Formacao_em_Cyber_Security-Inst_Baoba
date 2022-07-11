'''
Atividade 54

Criem um módulo chamado Operacoes que possua
as seguintes funções:

somar: Função que soma todos os elementos de
uma lista;

subtrair: Função que subtrai todos os elementos de
uma lista;

multiplicar: Função que multiplica todos os
elementos de uma lista;

dividir: Função que divide todos os elementos de
uma lista.

depois importe o módulo Operacoes e teste suas
funcionalidades.
'''


def somar(l):
    return sum(l)

def multi(l):
    total = 1
    for i in l:
        total *= i
    return total

def Subtrair(lista):
    total = lista[0] * 2
    for x in lista:
        total -= x
    return total

def Dividir(lista):
    total = 1
    for x in lista:
        total /= x
    return total



'''
#Operacoes.py
def Somar(lista):
    total = 0
    for x in lista:
        total += x
    return total
def Subtrair(lista):
    total = lista[0] * 2
    for x in lista:
        total -= x
    return total
def Multiplicar(lista):
    total = 1
    for x in lista:
        total *= x
    return total
def Dividir(lista):
    total = 1
    for x in lista:
        total /= x
    return total


#Teste.py
import Operacoes

nums = [1, 2, 3, 4, 5]

print(Operacoes.Somar(nums))
print(Operacoes.Subtrair(nums))
print(Operacoes.Multiplicar(nums))
print(Operacoes.Dividir(nums))
'''