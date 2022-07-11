# ****Atividade 6****
#
# Façam um programa que pergunta a idade do usuário.
# Se o usuário não for menor de idade, exiba uma mensagem de boas vindas.
# Caso o contrário, exiba uma mensagem informando que não é permitido menores de idade no estabelecimento.

idade = int(input("Informe sua idade: "))

str01 = 'Boas Vindas'
str02 = ' Não é permitido menores de idade no estabelecimento'

print(str01) if idade >= 18 else print(str02)

