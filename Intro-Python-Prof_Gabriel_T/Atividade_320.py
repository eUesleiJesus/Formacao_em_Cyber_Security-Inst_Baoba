'''
****Atividade 32****

- Façam um programa que imprima os inteiros de 1 a 50.
Para múltiplos de três imprima "Fizz" em vez do número e para os múltiplos de cinco imprima "Buzz".
Para números que são múltiplos de três e cinco, imprima "FizzBuzz".
'''

for i in range(1,51):

    if a == True and b == True:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
        a = True
    elif i % 3 == 0:
        print("Fizz")
        b = True
    else:
        print(i)