'''Crie um app de uma instituição bancária. O usuário poderá:

- Criar uma conta.
- Consultar os dados pessoais da conta.
- Alterar os dados pessoais da conta.
- Excluir a conta.

Com a conta criada, o usuário poderá realizar as seguintes operações:

- Consultar o saldo da conta.
- Depositar valor na conta.
- Sacar valor na conta.
- Sair do programa'''

import os

# tuplas
chaves = ('Nome Completo', 'Data de Nascimento', 'CPF', 'Profissão', 'Email','Endereço', 'Telefone')

# criação das contas e operações com as contas com lista e usuários
contas = []
conta = {}
operacoes = []
operacao = {}

os.system('cls')

while True:
    print('1- Criar uma conta.')
    print('2- Consultar os dados da conta.')
    print('3- Alterar os dados da conta.')
    print('4- Excluir a conta.')
    print('5- Sair do programa.')

    opcao = input('Opção do usuário: ')

    os.system('cls')

    match opcao:
        case '1':
            for i in range(len(chaves)):
                conta[chaves[i]] = input(f'Informe {chaves[i]}: ')
            contas.append(conta)
            print(f'\nConta criada com sucesso.')
            continue  
        case '2':
            

