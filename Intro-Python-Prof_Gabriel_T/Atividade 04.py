# ****Atividade 4****

## - Façam um Programa que peça 2 **números inteiros** e um **número real**. Calcule e mostre:
     #- o produto do dobro do primeiro com metade do segundo .
     #- a soma do triplo do primeiro com o terceiro.
     #- o terceiro elevado ao cubo.

### --- Programa

def fun_num(list):
    num_str = list

    if len(num_str) != 3:
        main()

    num_num = [float(string) for string in num_str]

    #- o produto do dobro do primeiro com metade do segundo .
    a = int((num_num[0]*2) * (num_num[1]/2))

    # - a soma do triplo do primeiro com o terceiro.
    b = int((num_num[0]*3)) + (num_num[2])

    # - o terceiro elevado ao cubo.
    c = (num_num[2]**3)

    return a, b, c

def main():
    list = input("Informe 2 numeros inteiros e 1 numero real: ").split()

    fun_num(list)

    a, b, c = fun_num(list)

    str01 = f""" 
            o produto do dobro do primeiro com metade do segundo: {a}
            a soma do triplo do primeiro com o terceiro: {b:.2f}
            o terceiro elevado ao cubo: {c:.2f}
            """

    print(str01)

main()