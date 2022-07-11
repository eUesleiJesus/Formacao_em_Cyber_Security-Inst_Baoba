# ****Atividade 16****
#
# - Façam um programa que receba um número inteiro e imprima a tabuada desse número até o 10.
#
# Dica: Com o print formatado, vocês podem escrever múltiplas variáveis. Exemplo:
#
# x = 1
#
# y = 2
#
# print(f"{x} + {y} = {x + y}") # resultado 1 + 2 = 3

x = int(input("informe um valor: "))
i = 0
y = 0

while i < 10:
    i += 1
    y += 1
    print(f"{x} X {y} = {x * y}")