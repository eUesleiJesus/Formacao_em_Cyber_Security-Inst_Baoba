# ****Atividade 7****
#
# • Façam um script que peça um valor e mostre na tela se o valor é positivo ou negativo,
# caso o número seja zero, mostre que o número não é positivo e nem negativo.

num = int(input(" Informe um numero: "))

str01 = ' O valor é positivo'
str02 = ' O número não é positivo e nem negativo '
str03 = ' O valor é negativo'

print(str01) if num > 0 else print(str02) if num == 0 else print(str03)