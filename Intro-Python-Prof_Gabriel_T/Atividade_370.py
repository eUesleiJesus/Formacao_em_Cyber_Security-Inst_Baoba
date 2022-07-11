"""
****Atividade 37****

Façam um programa que receba uma chave do usuário e cheque se ela pertence ao dicionário abaixo.

dicionario= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
dicionario = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dicionario["chave_nova"] = "valor novo"

for chave in dicionario:
    if "chave_nova" in {chave} and "valor novo" in {dicionario[chave]}:
        igual = True
    else:
        igual = False

print(igual)

'''
dicionario= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
chave = int(input("Digite uma chave "))
if chave in dicionario:
  print(f'A chave {chave } pertence ao dicionario')
else:
   print(f'A chave {chave } não pertence ao dicionario')


if'''