
# lista de notas
notas = []

# loop 
while True:
    # exibe menu
    print('1 - Inserir nota.')
    print('2 - Calcular a média das notas.')
    print('3 - Sair do programa.')

    # usuário informa a opção desejada
    opcao = input('Opção desejada: ')

    # verifica a opção desejada
    match opcao:
        case '1':
            # usuário informa nova nota
            nova_nota = str(input('Informe nova nota de 0 a 10: ')).replace(',', '.')

            # tenta verificar a nota
            try: 
                nova_nota = float(nova_nota)

                # verifica se a nota é maior que 0 e menor que 10
                if nova_nota >= 0 and nova_nota <= 10:
                    notas.append(nova_nota)
                    print(f'Nota {nova_nota} inserida com sucesso')
                else:
                    print('Nota inválida')
            except:
                print('Não foi possível inserir a nova nota.')
            finally:
                continue
        case '2':
            # calcula a média ou retorna erro
            try:
                media = sum(notas)/ len(notas)
                print(f'A média do aluno é {media:,.2f}')
            except:
                print('Não foi possível calcular a média.')
            finally:
                continue
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida')
            continue