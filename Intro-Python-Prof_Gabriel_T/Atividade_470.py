def calculadora(x, y, operacao):
    
    operacao = operacao
    if operacao == "adição":
        return x + y
    if operacao == "subtração":
        return x - y
    if operacao == "divisão":
        return x / y
    if operacao == "multiplicação":
        return x * y
    if operacao == "exponeciação":
        return x ** y
#
#teste
#operacao = "adição"
#operacao = "subtração"
#operacao = "divisão"
#operacao = "multiplicação"
operacao = "exponeciação"

x = 20
y = 10

print(calculadora(x, y, operacao))
