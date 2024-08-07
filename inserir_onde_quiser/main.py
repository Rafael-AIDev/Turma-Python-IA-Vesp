# lista de nomes
nomes = ['Fulano', 'Cicrano', 'Beltrano']

# usuário insere novo nome
novo_nome = input('Informe o novo nome: ').capitalize()  #capitaliza deixa a primeira letra maiúscula#
posicao =  int(input('Informe a posiçao do novo nome: '))

#insere o novo nome no local indicado
nomes.insert(posicao, novo_nome)

print('\n')

# imprime a lista
for nome in nomes:
    print(nome)

# ordenando a lista
nomes.sort()

print('\n')

# exibe a lista ordenada
for nome in nomes:
    print(nome)