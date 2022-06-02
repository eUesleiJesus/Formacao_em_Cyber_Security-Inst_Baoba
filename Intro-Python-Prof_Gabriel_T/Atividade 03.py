# ****Atividade 3****

## Façam um Programa que peça as 4 notas bimestrais e mostre a média.

### --- Programa
qnt_not = 4

def fun_not(list, qnt):

    Notas_str = list
    if len(Notas_str) != qnt:
        main(qnt)

    Notas_num = [int(string) for string in Notas_str]
    soma = sum(Notas_num)
    media = soma/(len(Notas_num))

    return media

def main(qnt_not):
    qnt = qnt_not
    list = input(f"Informe as {qnt} notas do Aluno: ").split()

    fun_not(list, qnt)

    media = fun_not(list, qnt)

    print(f"A media do aluno e: {media}")

main(qnt_not)

