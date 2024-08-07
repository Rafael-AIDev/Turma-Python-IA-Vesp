# entradada de dados
nome = input('Informe o nome do aluno: ')
nota = str(input('Informe a nota final: ')).replace(',', '.')

# convrsão 
nota = float(nota)

# verificação se a nota está entre 0 e 10
if nota <= 10 and nota >= 0:
    # verifica se o aluno foi aprovado
    if nota >= 7:
        print(f'{nome} está aprovado.')
    elif nota >= 5:
        print(f'{nome} está de recuperação.')
    else:
        print(f'{nome} está reprovado.')
else:
    print('Nota inválida.')