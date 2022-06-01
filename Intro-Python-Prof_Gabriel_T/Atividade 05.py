# ****Atividade 5****

## • Faça um programa que receba o faturamento e o custo de uma venda,
## calcule o lucro e depois
## calcule e imprima a margem de lucro(lucro/ faturamento) com somente duas casas decimais.

### --- Programa

def fun_lucro():
    val_str = input("Informe o faturamento e o custo: ").split()

    if len(val_str) != 2:
        fun_lucro()

    val_num = [int(string) for string in val_str]
    lucro = val_num[0] - val_num[1]
    margem = lucro / val_num[0]
    print(f" O Lucro foi de: {lucro:.2f}$, e a margem foi de: {margem:.2%}")

fun_lucro()