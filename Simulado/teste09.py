'''
Dada as duas lista abaixo,
faça um programa que preencha uma terceira lista,
com somente os números múltiplos de 18 das duas listas:

'''
a = [162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, ]
b = [189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216]
lista = a + b
multipl = []

for i in lista:
    if i % 18 == 0:
        multipl.append(i)


print(multipl) # [162, 180, 198, 216] *
