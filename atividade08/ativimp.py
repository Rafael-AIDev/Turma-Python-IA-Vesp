# importação de biblioteca
import os
from datetime import date

nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
data = f'{date.today().day}/{date.today().month}/{date.today().year}'
# limpa console
os.system('cls')

#início do loop
while True:
    print(f'{'='*30} CINE PYTHON {'='*30}\n')
    print('Sala 1 - A Volta dos que não foram - 12 anos')
    print('Sala 2 - A Roda Quadrada - Livre')
    print('Sala 3 - Poeira em alto mar - 14 anos')
    print('Sala 4 - As traças do Rei careca - 16 anos')
    print('Sala 5 - A Vinguança do peixe frito - 18 anos')
    # escolha da sala
    sala = input('\nSala desejada: ')

    # limpa console
    os.system('cls')
    # verifica a sala escolhida
    match sala: 
        case '1':
            idade_minima = 12
            filme = 'A Volta dos que não foram'
        case '2':
            idade_minima = 0
            filme = 'A Roda Quadrada'
        case '3':
            idade_minima = 14
            filme = 'Poeira em alto mar'
        case '4':
            idade_minima = 16
            filme = 'As traças do Rei careca'
        case '5':
            idade_minima = 18
            filme = 'A Vinguança do peixe frito'
        case _:
            print('Sala inexistente. Favor escolher outra sala')
            continue

    # verificação da idade
    if idade >= idade_minima:
        print(f'Ingresso impresso no dia {data}.\n')
        print(f'Pagante {nome}.')
        print(f'Filme {filme}.')
        print(f'Sala {sala}.\n')
        print(f'Tenha um ótimo filme!')
        break
    else: 
        print(f'{nome} não possui a idade mínima para ver o {filme}.')
        print('Favor escolher outro filme')
        continue