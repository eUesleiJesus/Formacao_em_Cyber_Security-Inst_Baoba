# ****Atividade 21****
#z
# - Façam um programa que adicione 3 valores recebidos pelo usuário na lista abaixo.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nova_str = input("informe os novos valores: ").split()
nova_num = [int(string) for string in nova_str]

for i in nova_num:
    lista.append(i)
    
print(lista)