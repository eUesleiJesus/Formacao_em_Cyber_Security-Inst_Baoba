'''
Façam uma função que retorna a quantidade de vogais e consoantes de uma palavra.
'''

def func(meunome):
    vogal = 0
    cons = 0
    for i in meunome:
        if i == "a" \
            or i == "e" \
            or i == "i" \
            or i == "o"\
            or i == "u"\
            or i == "A" \
            or i == "E" \
            or i == "I" \
            or i == "0" \
            or i == "U":

            vogal += 1
        else:
            cons += 1
    print(vogal, cons)
    return(vogal, cons)

meunome = "meunome"
func(meunome)

'''
def vog_con(palavra):
  vog = 0
  con = 0
  for letra in palavra:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
      vog += 1
    else:
      con += 1
  return vog, con


print(vog_con("lIma"))
'''