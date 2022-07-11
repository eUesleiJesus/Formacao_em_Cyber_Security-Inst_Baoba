'''
****Atividade 33****

- Façam um programa que imprima todos os números primos entre 25 e 50 utilizando dois for loops.
'''
c = 0

for x in range(25, 51):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        print(x)

