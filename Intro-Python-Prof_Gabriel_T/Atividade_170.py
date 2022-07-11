#****Atividade 17****
# Façam um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido

def erro():
    print("Err0!")
    main()

def main():
    nota = int(input("informe uma nota: "))
    if nota > 10:
        erro()
    elif nota < 0:
        erro()
    else:
        print(f" A nota e : {nota}")

main()