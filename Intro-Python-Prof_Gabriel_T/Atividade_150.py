#****Atividade 15****
# Façam um programa que receba um valor do usuário e faça a contagem regressiva dele até o zero.

n = int(input("informe um valor: "))
i = 0
t = n

while i < n + 1:

    print(t)
    t -= 1

    i += 1