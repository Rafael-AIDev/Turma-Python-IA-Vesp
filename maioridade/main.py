# executando loop infinito
while True:
    # entrada de dados
    nome = input('Informe o seu nome: ')
    idade = int(input('Informe sua idade: '))

    # verifica a maioridade do usuário
    if idade >= 18:
        print(f'{nome} é maior de idade')
    else:
        print(f'{nome} é menor de idade')

    # verifica se o usuário deseja continuar
    continuar = input('Deseja continuar (s/n)? ').lower()

    # verifica a opção do usuário
    if continuar == 's':
        continue
    else:
        break