'''Façam uma função que receba uma quantidade indeterminada  de argumentos  e imprima  seus valores'''

def func(*args):
    for i in args:
        print(i)
    print(args)

func(10, 20, 30)
func(40, 50)