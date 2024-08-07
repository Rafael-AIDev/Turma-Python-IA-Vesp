# lista
nomes = ['Fulano', 'Cicrano', 'Beltrano', 'Beltrano', 'João', 'Maria', 'José']

# exibe a lista e seus respectivos índices
for i in range(len(nomes)):
    print(f'Índice {i}: {nomes[i]}.')

# quebra de linha
print('\n')

try:
    # usuário informa o índice
    indice = int(input('Informe o número do índice: '))

    # faz a alteração
    nomes[indice] = input('Informe um novo nome: ')
except:
    print('Não foi possível fazer a alteração.')

# exibe a nova lista
for i in range(len(nomes)):
    print(f'Indice {i}: {nomes[i]}.')
