# declaração de variáveis
nome: str = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))

# verificação da idade
if idade >= 18: 
    print(f'{nome} é maior de idade.')
else: 
    print(f'{nome} é menor de idade.')