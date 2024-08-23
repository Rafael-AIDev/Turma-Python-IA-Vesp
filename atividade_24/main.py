'''Crie um programa em que o usuário cria uma lista de nomes na quantidade que ele desejar, e o programa sorteia o nome dele.'''
import random
# biblioteca random gera número aleatórios

nomes = []

while True:
    print('1- Inserir nome na lista.')
    print('2- Sortear.')
    print('3- Sair do programa.')

    opcao = input('Opção desejada: ')

    match opcao:
        case '1':
            nome = input('Insira o nome: ')
            nomes.append(nome)
            print(f'{nome} inserido com sucesso')
            continue
        case '2':
            indice_sorteado = random.randint(0, len(nomes)-1) # esse -1 serve para não ultrapassar o indice da lista, tipo um stop
            print(f'Nome sorteado: {nomes[indice_sorteado]}')
            continue
        case '3':
            print('Programa encerrado')
            break
        case _:
            print('Opção inválida')
            continue

