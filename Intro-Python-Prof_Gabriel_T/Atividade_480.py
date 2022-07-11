''''**Atividade 48**

Façam uma função que:

Receba a quantidade de lados de um dado;

Imprima um valor aleatório de 1 até o número de
lados, utilizando a biblioteca random e a função
random.randint().

randint(a, b) retorna um número inteiro entre a e b.'''
import random
from random import  randint
lados_dado = 20

valor = random.randint(1, lados_dado)

if valor == 0:
    print(valor, " Erro Crítico")
if valor == 20:
    print(valor, " Acerto Crítico")
else:
    print(valor)

''''
import random

def roll(lados):
    print(f"Você rolou um D{lados}! \nO resultado foi {random.randint(1,lados)}.")

roll(20)
'''