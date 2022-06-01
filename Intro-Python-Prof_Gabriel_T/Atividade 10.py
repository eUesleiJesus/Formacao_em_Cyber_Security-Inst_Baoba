# ****Atividade 10****
#
# • Façam um Programa que Leia três números e que imprima o maior e o menor.


list_ste = input("Informe 3 numeros ").split()

if len(list_ste) != 3:
    fun_maior()

list_num = [int(string) for string in list_ste]

print(f"O menor valor e : {min(list_num)} \n"
      f"o maior valor e : {max(list_num)}")
