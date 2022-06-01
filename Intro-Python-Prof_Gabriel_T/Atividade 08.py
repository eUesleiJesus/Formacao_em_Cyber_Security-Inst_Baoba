# ****Atividade 8****
#
# • Façam um programa que receba um número inteiro e verifique se este número é par ou ímpar.

num = int(input(" Informe um numero: "))

str01 = ' é par'
str02 = ' é ímpar '

print(str01) if (num%2) == 0 else print(str02)