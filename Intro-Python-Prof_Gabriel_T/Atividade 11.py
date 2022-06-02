#****Atividade 11****
#
# • Façam um programa que pergunte o salário do funcionário e calcule o valor do aumento.
#   Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#   Para os inferiores ou iguais, de 15%.

salario = float(input("Informe o Salario: "))

if salario > 1250:
    salario += salario*0.1
    print(f"Parabens, voce recebeu um aumento de 10% seu novo salario e : {salario:.2f}$")
else:
    salario += salario*0.15
    print(f"Parabens, voce recebeu um aumento de 15% seu novo salario e : {salario:.2f}$")
