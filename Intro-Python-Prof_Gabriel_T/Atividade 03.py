# ****Atividade 3****

## Façam um Programa que peça as 4 notas bimestrais e mostre a média.

### --- Programa

def fun_not():
    Notas_str = input("Informe as 4 notas do Aluno: ").split()

    if len(Notas_str) != 4:
        fun_not()

    Notas_num = [int(string) for string in Notas_str]
    soma = sum(Notas_num)
    media = soma/(len(Notas_num))
    print(f"A media do aluno e: {media}")

fun_not()