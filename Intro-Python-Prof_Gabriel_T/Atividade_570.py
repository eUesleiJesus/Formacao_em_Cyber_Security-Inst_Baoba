'''
faça um Aluno com:
Atributo: nome, matricula e um array de notas

metodos: media(calcule e imprime a media do aluno)
e ponto_extra(aumenta uma nota escolhida)
'''

class Aluno():
    def __init__(self, nome, matricula, notas):
        self.__nome = nome
        self.__matricula = matricula
        self.__notas = notas

    def media(self):
        total = sum(self.__notas)
        num_notas = self.__notas
        med = total / len(num_notas)
        print(f' média = { med }')

    def ponto_exta(self, numero_nota, incremeto):
        if numero_nota <=len(self.__notas):
            self.__notas[numero_nota - 1] += incremeto
            return
        print(("Nota não existe"))

notas = [10, 7, 5, 4]
ueslei = Aluno("Ueslei", 8445452, notas)

Aluno.media(ueslei)
Aluno.ponto_exta(ueslei, 4, 7)
Aluno.media(ueslei)

'''
class Aluno():
    def __init__(self, nome, matricula, notas):
        self.__nome = nome
        self.__matricula = matricula
        self.__notas = notas

    def media(self):
        total = 0
        for i in range(0, len(self.__notas)): #ou total = sum(self.__notas)
            total += self.__notas[i]
        print(f'{self.__nome} tem uma media de {total / len(self.__notas) : .2f}')

    def ponto_extra(self, numero_nota, incremento):
        if numero_nota <= len(self.__notas):
            self.__notas[numero_nota - 1] += incremento
            return
        print("Nota nao existe.")

aluno = Aluno("Alberto", 1851354234, [7, 4, 8, 3, 10])
aluno.media()
aluno.ponto_extra(4, 7)
aluno.media()
'''