# ****Atividade 13****
#
#
#
# - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
# - 1- Soma de 2 números.
# - 2- Diferença entre 2 números (maior pelo menor).
# - 3- Produto entre 2 números.
# - 4- Divisão entre 2 números (o denominador não pode ser zero).
# - dica vocês podem pular a linha em um print usando \n

def invalido():
    print("Err0!")
    main()

def convert(lista):
    lista = lista
    val_num = [int(string) for string in lista]
    return val_num

def soma(lista):
    valor = lista
    valor = valor[0] + valor[1]
    return valor

def divisao(lista):
    valor = lista

    if valor[1] == 0:
        invalido()

    valor = lista[0] / lista[1]

    return valor

def produto(lista):
    valor = lista
    valor = valor[0] * valor[1]
    return valor

def diferenca(lista):

    valor = lista

    if valor[0] > valor[1]:
        valor = valor[0] - valor[1]
    elif valor[0] < valor[1]:
        valor = valor[1] - valor[0]
    else:
        valor = 0
    return valor

def main():
    menu = int(input("""
    
    # - 1- Soma de 2 números.
    # - 2- Diferença entre 2 números (maior pelo menor).
    # - 3- Produto entre 2 números.
    # - 4- Divisão entre 2 números (o denominador não pode ser zero).
          
    """))

    if menu == 1:
        lista = input("Informe os dois numeros: \n").split()
        valor = convert(lista)
        soma_valor = soma(valor)
        print(f" \n A soma de {valor[0]} + {valor[1]} e igual a {soma_valor}")

    elif menu == 2:
        lista = input("Informe os dois numeros: \n").split()
        valor = convert(lista)
        sub_valor = diferenca(valor)

        if valor[0] > valor[1]:
             print(f" \n A diferença de {valor[0]} - {valor[1]} e igual a {sub_valor}")
        elif valor[0] < valor[1]:
             print(f" \n A diferença de {valor[1]} - {valor[0]} e igual a {sub_valor}")
        else:
            print(f" \n A diferença de {valor[1]} - {valor[0]} e igual a {0}")


    elif menu ==3:
        lista = input("Informe os dois numeros: \n").split()
        valor = convert(lista)
        pro_valor = produto(valor)
        print(f" \n O Produto de de {valor[0]} X {valor[1]} e igual a {pro_valor}")

    elif menu == 4:
        lista = input("Informe os dois numeros: ").split()
        valor = convert(lista)
        div_valor = divisao(valor)
        print(f" \n A razao de {valor[0]} por {valor[1]} e igual a {div_valor:.2f}")


    else :
        invalido()

main()

