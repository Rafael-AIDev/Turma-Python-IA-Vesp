# importação de biblioteca
import os 
import time

# entrada de dados
numero = int(input('Informe um número inteiro: '))

while numero >= 0:
    os.system('cls')
    print('\nContagem regressiva:')
    print(f'{numero}...')
    numero -= 1
    time.sleep(1)

os.system('cls')
print('KABUMMM')