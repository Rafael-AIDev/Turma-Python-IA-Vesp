# dicionário
usuario = {
    'Nome': 'Alex Ribeiro',
    'Idade': 39,
    'Profissão': 'programador'
}

# adicionar uma nova chave ao dicionário
usuario['Email'] = input('Informe o e-mail do usuário: ')

# alterando o valor de uma chave
usuario['Nome'] = input('Informe o novo nome: ')

# excluindo a chave
del usuario['Idade']

# exibindo valores do dicionário na tela
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')


