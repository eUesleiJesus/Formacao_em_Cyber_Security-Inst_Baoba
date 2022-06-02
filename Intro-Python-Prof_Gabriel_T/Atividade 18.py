# ****Atividade 18****
#
# Façam um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

def erro():
    print("Err0!")
    main()

def main():
    login = input("informe o nome de usuario: ")
    senha = input("informe a senha: ")

    if login == senha:
        erro()

main()