'''
Atividade 50

Façam uma função utilizando random.choice() que:

Guarde as lista abaixo em uma lista;

Selecione uma das listas abaixo;

Imprima um de seus elementos aleatoriamente;

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

let = ["a", "b", "c", "d", "e"]

tf = [True,False,None]

random.choice(x) escolhe um item de x.
'''
import random
from random import choice


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

let = ["a", "b", "c", "d", "e"]

tf = [True,False,None]

def list(*args):
    Lista = [num, let, tf]

    print(random.choice(random.choice(Lista)))

list(num, let, tf)

"""
---------ATIVIDADE 50----------------------
import random

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let = ["a", "b", "c", "d", "e"]
tf = [True,False,None]


def item_aleatorio(l1,l2,l3):
    listas = [l1,l2,l3]
    escolhido = random.choice(listas)
    print(random.choice(escolhido))
item_aleatorio(num,let,tf)
"""