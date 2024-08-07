# entrada de dados
nome = input('Informe seu nome: ')

# lista de cursos
print(f'{'='*30} LISTA DE CURSOS {'='*30}\n')
print('1 - Operador de Micro.')
print('2 - Desenvolvedor Java.')
print('3 - Dsenvolvedor Python.')
print('4 - Desenvolvedor Front-End.')
print('5 - Montador e Reparador de Micro.')

# seleção de cursos
opcao = input('\nEscolha sua opção de curso: ')

# o "switch...case " do python
match int(opcao):
    case 1:
        print(f'{nome} se matriculou no Operador de Micro.')
    case 2:
        print(f'{nome} se matriculou no Desenvolvedor Java.')
    case 3:
        print(f'{nome} se matriculou no Desenvolvedor Python')
    case 4:
        print(f'{nome} se matriculou no Front-End.')
    case 5:
        print(f'{nome} se matriculou no Montador e Reparador de Micro ')
    # default
    case _:
        print('Opção inválida.')