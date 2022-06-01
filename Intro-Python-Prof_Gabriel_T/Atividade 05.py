# ****Atividade 5****

## • Faça um programa que receba o faturamento e o custo de uma venda,
## calcule o lucro e depois
## calcule e imprima a margem de lucro(lucro/ faturamento) com somente duas casas decimais.

### --- Programa

def lucro():
    val_str = input("Informe ao faturamento e o custo: ").split()

    if len(Notas_str) != 2:
        fun_not()

    Notas_num = [int(string) for string in Notas_str]
    soma = sum(Notas_num)
    media = soma/(len(Notas_num))
    print(f"A media do aluno e: {media}")

fun_not()