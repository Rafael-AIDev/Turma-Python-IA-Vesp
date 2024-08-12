'''Crie um programa que receba os dados de um usuário, armazene-os em um dicionário, e os informe na tela. Os dados cadastrais serão os mesmos encontrados no gerador de pessoas do site 4 devs (em anexo). Ao terminar, envie o link do repositório.'''

# dicionário
usuario = {}

usuario['Nome'] = input('Informe o nome: ')
usuario['CPF'] = input('Informe o CPF: ')
usuario['RG'] = input('Informe o RG: ')
usuario['Data_de_Nascimento'] = input('Informe a data de nascimento: ')
usuario['Sexo'] = input('Informe o sexo: ')
usuario['Signo'] = input('Informe o Signo: ')
usuario['Mae'] = input('Informe o nome da mãe: ')
usuario['Pai'] = input('Informe o nome do pai: ')
usuario['Email'] = input('Informe o email: ')
usuario['Senha'] = input('Informe a senha: ')
usuario['CEP'] = input('Informe o CEP: ')
usuario['Endereco'] = input('Informe o endereço: ')
usuario['Numero'] = input('Informe o número: ')
usuario['Bairro'] = input('Informe o bairro: ')
usuario['Cidade'] = input('Informe a cidade: ')
usuario['Estado'] = input('Informe o Estado: ')
usuario['Telefone'] = input('Informe o telefone: ')
usuario['Celular'] = input('Informe o celular: ')
usuario['Altura'] = input('Informe a altura em cm: ').replace(',', '.')
usuario['Peso'] = input('Informe o peso em kg: ').replace(',', '.')
usuario['Sangue'] = input('Informe o tipo sanguíneo: ')
usuario['Cor'] = input('Informe a cor favorita: ')

for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')