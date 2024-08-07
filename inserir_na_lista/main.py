# lista
cobras = ['Sucuri', 'Piton', 'Mamba Negra', 'Naja']

# exibe a lista original
for cobra in cobras:
    print(cobra)

# usuário informa o nome da nova cobra
nova_cobra = input('\nInforme o nome da nova cobra: ')

# insere a nova cobra na lista
cobras.append(nova_cobra)

print('\n')

# exibe a nova lista
for cobra in cobras:
    print(cobra)

# ordenar a lista
cobras.sort()

# exibe a lista ordenada
for cobra in cobras:
    print(cobra)