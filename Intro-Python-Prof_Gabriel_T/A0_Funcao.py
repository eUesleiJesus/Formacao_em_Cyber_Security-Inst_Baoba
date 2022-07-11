def criar_lista_num(list_str):
    list_str = list_str.split()
    list_num = [int(string) for string in list_str]
    return list_num

def media(list):
    soma = sum(list)
    media = sum(list) / len(list)
    return media

