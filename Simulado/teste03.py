'''
Considerando como dados, o ano de entrada e aluguel de uma casa,
 construa um algoritmo que calcula o reajuste de um aluguel,
 utilizando as seguintes fórmulas:

entradas posteriores a 2015: (aluguel * 1,18)
entradas iguais ou anteriores a 2015: (aluguel * 1,15)
peça o aluguel e a data de entrada do usuário e informe o novo valor após o reajuste


peça o aluguel e a data de entrada  do usuário  e
 informe o novo valor  após o reajuste.
'''

aluguel, data = input("Informe o aluguel e a data: ").split()
aluguel = int(aluguel)
data = int(data)

if data > 2015:
    aluguel *=1.18
else:
    aluguel *=1.15

print(f"novo aluguel = {aluguel: .2f}")
