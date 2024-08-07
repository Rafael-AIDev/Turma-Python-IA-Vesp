'''Crie um programa que receba uma notas de avaliações em uma quantidade definida pelo usuário, calcula a média e exibe o resultado. Ao terminar envie para o repositório do GitHub e poste o link.'''
notas = []

# ínicio do loop
while True:
    # menu
    print('1 - Inserir nova nota da avaliação: ')
    print('2 - Exibir resultado da média das notas de avaliação')
    print('3 - Exibir notas dadas')
    print('4 - Sair do programa')

    opcao = input('\nOpção do usuário: ')

    match opcao:
        case '1':
            nova_nota = int(input('Insira a nova nota: '))
            notas.append(nova_nota)
            print(f'{nova_nota} adicionada com sucesso.')
            continue
        case '2':
            notas.sort(reverse=True)
            for nota in notas:
                print(nota, end=' - ')

            media = sum(notas)/len(notas)
            print(f'\nResultado da média é {media:,.2f}')
            continue
        case '3':
            print('Lista de notas de avaliação:')
            for nota in notas:
                print(nota, end=' - ')
            continue
        case '4':
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida')
            
