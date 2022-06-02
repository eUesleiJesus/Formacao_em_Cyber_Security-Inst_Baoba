# ****Atividade 5****

## • Faça um programa que receba o faturamento e o custo de uma venda,
## calcule o lucro e depois
## calcule e imprima a margem de lucro(lucro/ faturamento) com somente duas casas decimais.

### --- Programa

def fun_lucro(list):
    val_str = list

    if len(val_str) != 2:
        main()

    val_num = [int(string) for string in val_str]
    lucro = val_num[0] - val_num[1]
    margem = lucro / val_num[0]

    return lucro, margem


def main():
    list = input("Informe o faturamento e o custo: ").split()

    fun_lucro(list)

    lucro, margem = fun_lucro(list)
    if lucro > 0:
        print(f" O Lucro foi de: {lucro:.2f}$, e a margem foi de: {margem:.2%}")
    else:
        print(f" O prejuizo foi de: {lucro:.2f}$, e a margem foi de: {margem:.2%}")


main()