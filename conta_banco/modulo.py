# importa função de data
from datetime import date

# função exibir menu
def exibir_menu():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'\n{'='*20} BANCO ANACONDA | {dia}/{mes}/{ano} {'='*20}\n ')
    print(f'1 - Criar conta')
    print(f'2 - Entrar na conta')
    print(f'3 - Exibir correntista')
    print(f'4 - Excluir conta')
    print(f'5 - Encerrar programa')

# função exibir operações
def exibir_operacoes():
    print('\nOPERAÇÕES\n')
    print('1 - Consultar saldo')
    print('2 - Depositar valor')
    print('3 - Sacar valor')
    print('4 - Voltar')

# função exibir daddos do correntista
def exibir_dados(nome, i, saldo):
    print(f'ID: {i}')
    print(f'Nome: {nome}')
    print(f'Agência: 1001')
    print(f'Conta: 1001{i}')
    print(f'Saldo: {saldo}')

# função de depósito
def depositar_valor(saldo, valor):
    saldo += valor
    return saldo

# função de saque
def sacar_valor(saldo, valor):
    saldo -= valor
    return saldo
