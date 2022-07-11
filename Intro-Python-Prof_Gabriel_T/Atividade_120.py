#****Atividade 12****
#
# • Façam um Programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até de 200 km,
# e R$ 0,45 para viagens mais longas.


def valor(km):
    dist = km
    if dist > 200:
        custo = dist * 0.5
        return custo
    else:
        custo = dist * 0.45
        return custo


def main():
    dist = int(input("informe a distancia que sera percorrida: "))

    custo = valor(dist)

    print(f" o custo da viagem sera de {custo:.2f}$")

main()