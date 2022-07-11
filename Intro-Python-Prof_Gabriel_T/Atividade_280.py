'''
****Atividade 28****

- Façam um programa que imprima os valores do que não repetem entre os conjuntos.

conjunto1 = {10, 20, 30, 40, 50}

conjunto2 = {30, 40, 50, 60, 70}
'''

conjunto1 = {10, 20, 30, 40, 50}

conjunto2 = {30, 40, 50, 60, 70}

print(conjunto1.union(conjunto2)-conjunto1.intersection(conjunto2))