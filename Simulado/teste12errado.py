'''
Faça um programa que leia um nome de usuário e
uma senha, onde eles não podem se repetir.
Depois peça para o usuário se logar
Caso ele digite as informações corretas imprima
a mensagem “Seja bem-vindo (nome do usuário)!”.
Caso contrário repita o teste de login até ele
ser preenchido corretamente.
*
'''

'''
def login():
    nome, senha = input("informe o nome e a senha: ").split()
    if nome == senha:
        login()
    return nome, senha

def main():
    nome, senha = login()
    print(f'Seja bem-vindo {nome}!')

main()
'''

def cadastro():
    nome = input("informe o nome do cadastro: ")
    senha = input("crie  uma senha: ")
    if nome == senha:
        cadastro()
    return nome, senha

def login(nome, senha):
    nome_entrada = input("informe o login: ")
    senha_entrada = input("informe a senha: ")
    nome_login = nome
    senha_login = senha
    if nome_entrada == nome and senha_entrada == senha:
       return True
    else:
        login()


def main():
    nome, senha = cadastro()
    login(nome, senha)
    if login == True:
        print(f'Seja bem-vindo {nome}!')

main()