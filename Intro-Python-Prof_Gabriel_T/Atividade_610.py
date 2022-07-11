'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
(a)Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
	(i) tipoCombustivel.
	(ii) valorLitro
	(iii) quantidadeCombustivel

(b)Possua no mínimo esses métodos:
	(i) abastecerPorValor( ) – método onde é informado o valor a ser abastecido e
	mostra a quantidade de litros que foi colocada no veículo
	(ii) abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e
	mostra o valor a ser pago pelo cliente.
	(iii) alterarValor( ) – altera o valor do litro do combustível.
	(iv) alterarCombustivel( ) – altera o tipo do combustível.
	(v) alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

'''

class bombaCombustivel():
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.__tipoCombustivel       = tipoCombustivel
        self.__valorLitro            = valorLitro
        self.__quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.__valorLitro
        if(self.__quantidadeCombustivel - litros > 0):
            self.__quantidadeCombustivel -= litros
            print(f'Foram colocados {litros:.2f}L em seu veiculo.')
            return
        print(f'Nao ha combustivel suficiente na bomba para abastecer {litros:.2f}L.')
        print(f'Combustivel restante: {self.__quantidadeCombustivel:.2f}L.')

    def abastecerPorLitro(self, litros):
        if(self.__quantidadeCombustivel - litros > 0):
            valor = litros * self.__valorLitro
            self.__quantidadeCombustivel -= litros
            print(f'Foram colocados {litros:.2f}L em seu veiculo.')
            print(f'Voce deve R${valor:.2f}.')
            return
        print(f'Nao ha combustivel suficiente na bomba para abastecer {litros:.2f}L.')
        print(f'Combustivel restante: {self.__quantidadeCombustivel:.2f}L.')

    def alterarValor(self, valor):
        self.__valorLitro = valor
    def alterarCombustivel(self, tipoCombustivel):
        self.__tipoCombustivel = tipoCombustivel
    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.__quantidadeCombustivel = quantidadeCombustivel

bomba = bombaCombustivel("Diesel", 4.57, 1280)
bomba.abastecerPorValor(38.95)
bomba.abastecerPorLitro(80)
bomba.alterarValor(0.01)
bomba.abastecerPorLitro(482.547)
