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

def soma():
    list = input("Informe o dois numeros: ").split()
    val_num = [int(string) for string in list]
    sum = val_num[0] + al_num[1]
    print(f" a soma de {val_num[0]} + {val_num[1]} e igual a {sum}")

def diferenca():

def produto():

def divisao():

def erro():

def main():
    menu = int(input("""
    
    # - 1- Soma de 2 números.
    # - 2- Diferença entre 2 números (maior pelo menor).
    # - 3- Produto entre 2 números.
    # - 4- Divisão entre 2 números (o denominador não pode ser zero).
          
    """))

    if menu == 1:
        soma()
    elif menu == 2:
        deferenca()
    elif menu ==3:
        produto()
    elif menu == 4:
        divisao()
    else :
        erro()

main()