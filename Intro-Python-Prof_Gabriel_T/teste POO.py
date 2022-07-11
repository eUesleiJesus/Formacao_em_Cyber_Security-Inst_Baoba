class Aluno():
 def __init__(self, nota, matricula):
  self.nota = nota
  self.matricula = matricula

 def mostrar(self):
  print("a nota é", self.nota)
  print("a matricula é", self.matrcula)

  pedro = Aluno(7, 2121321)
  pedro.mostrar(self)

  '''
  class Aluno:
  def __init__(self,nom, nt,mat):
     self.nome = nom
     self.nota = nt
     self.matricula = mat
  def apresentacao(self):
     print(f"Olá, sou {self.nome}!")
  def escola(self):
     print("Você estuda na escola x")

class Turma_01(Aluno):
  def horario(self):
     print("Sua aula começa 7h!")

class Turma_02(Aluno):
  def horario(self):
     print("Sua aula começa 13h!")

Joao = Turma_01("a",1,2)
Joao.escola()
Joao.horario()
Pedro = Turma_02("a",1,2)
Pedro.escola()
Pedro.horario()
'''