# ****Atividade 9****
#
# • Façam um programa que pergunte a velocidade do carro de um usuário.
#   Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
#   Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

num = int(input(" Informe a velocidade: "))

multa = (num-80)*5

str01 = f' Voce foi multado, sua multa e de : {multa:.2f}$'
str02 = "Sem multa"

if num > 80:
    print(str01)
else:
    print(str02)