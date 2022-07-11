"""

****Atividade 3****

Façam um Programa que peça as 4 notas bimestrais e mostre a média.

Programa
"""
"""
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
    
    

    fun_not(list, qnt)

    media = fun_not(list, qnt)

    print(f"A media do aluno e: {media}")

main(qnt_not)
"""

from A0_Funcao import criar_lista_num, media

def main():
    texto = "Informe as 04 notas bimestrais: ex(10 5 6 8) \n"
    notas_str = input(texto)

    notas = criar_lista_num(notas_str)

    media_aluno = media(notas)

    texto = f"\n A media do aluno é {media_aluno: .2f}"
    print(texto)

main()

