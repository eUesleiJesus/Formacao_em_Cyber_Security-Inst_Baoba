"""
faça uma função que receba 3 números inteiros do usuário e retorne o maior entre eles
"""
def maior(a, b, c):
    maior = a

    if b > maior:
        maior = b
    if c > maior:
        maior = c

    return maior