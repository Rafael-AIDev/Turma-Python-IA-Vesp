# funçãp de boas vindas
def saudar(nome,idade):
    print(f'{nome}, bem vindo.' if idade >= 18 else f'{nome} foi bloqueado') # 2ª forma com ternário
# programa principal
nome = input('Informe o seu nome: ')
idade = int(input('Informe sua idade: '))

# executando a função
saudar(nome,idade)
