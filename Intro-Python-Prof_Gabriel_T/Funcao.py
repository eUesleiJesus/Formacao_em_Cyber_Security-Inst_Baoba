def printar_texto(text):
    print(text)

def mostrar_num(num):
    print(num)

def perguntar_num():
   num = int(input("Digite um numero: "))
   return num

def criar_lista_num():
    list_str = input().split()
    list_num = [int(string) for string in list_str]
    return list_num

def media(list):
    soma = sum(list)
    media = sum(list) / len(list)
    return media

