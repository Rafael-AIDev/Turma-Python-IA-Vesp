'''Crie um programa que receba o valor atual da gasolina e do etanol,
 e verifica qual o melhor combustível para um carro flex abastecer. Ao terminar, envie o arquivo .py.'''

# entrada de dados
gasolina = str(input('Informe o preço da gasolina: R$ ')).replace(',', '.')
etanol = str(input('Informe o preço da etanol: R$ ')).replace(',', '.')

# conversão
gasolina = float(gasolina)
etanol = float(etanol)

# verificação dos valores
if etanol > gasolina * 0.7:
    print('É melhor abastecer com gasolina.')
else: 
    print('Melhor abastecer ccom etanol.')