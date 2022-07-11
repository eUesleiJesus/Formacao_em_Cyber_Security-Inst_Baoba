'''
****Atividade 40****

- Façam um programa que calcule o produto dos valores do dicionário abaixo.

dicionario = {'n1':100,'n2':-54,'n3':247}
'''
dicionario = {'n1':100,'n2':-54,'n3':247}
produto = 1
for item in dicionario:

    produto *= dicionario[item]
print(produto)
