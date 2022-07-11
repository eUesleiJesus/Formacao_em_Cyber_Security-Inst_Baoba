"""

****Atividade 2****

• Façam um Programa que peça um número e então mostre a mensagem
“*O número informado foi {número}*.”

Programa
"""
from Atividade_000 import mostrar_texto, perguntar_num

def main():
    num = perguntar_num()
    texto = (f'O número informado foi {num}')
    mostrar_texto(texto)
main()

