'''

Atividade 53

Criem um módulo chamado Notas, que receba 4
notas de um aluno e possui as seguinte funções:

média: Calcula e retorna a média do aluno;

resultado: Verificar se o aluno possui uma média
acima de 7, e retornar se ele está aprovado ou
reprovado;

Depois importe o módulo Notas e teste suas
funcionalidades.
'''

def resultado(media):
    if media >= 7:
       return print("aprovado")
    else:
       return print("reprovado")

def media(x, y, z, w):
    media = (x+y+z+w)/4

    return media

'''
#Notas.py
def Media (n1,n2, n3, n4):
    media = (n1 + n2 +n3 + n4) / 4
    return  media
def Resultado(media):
    if media >= 7:
        print("Você está aprovado!")
    else:
        print("Você está reprovado.")
#Teste.py

import Notas


print(Notas.Media(7,5,10,9))
print(Notas.Resultado(7.75))
'''