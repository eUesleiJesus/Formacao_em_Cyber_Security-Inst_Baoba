'''
Faça um programa
que remova os itens dos dois conjuntos abaixo,
que não são comuns a ambos.

remova os itens que não se repetem

pergunta confusa

'''
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print(set3) # {40, 50, 30}#
'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
set2.intersection_update(set1)
print(set1, set2)