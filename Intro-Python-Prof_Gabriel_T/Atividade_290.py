'''
****Atividade 29****

- Façam um programa que adiciona os itens do conjunto 2 ao conjunto 1 se o item não for repetido.

set1 = {10, 20, 30, 40, 50}

set2 = {30, 40, 50, 60, 70}
'''


set1 = {10, 20, 30, 40, 50}

set2 = {30, 40, 50, 60, 70}

set1.update(set2)

print(set1)
