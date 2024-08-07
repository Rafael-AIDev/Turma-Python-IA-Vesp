# entrada de dados
x = input('Informe um número: ')
y = input('Informe outro número: ')

# tratamento de exceções
try:
    multiplicacao = int(x) * int(y)
    print(f'O resultado da multiplicação é {multiplicacao}')
except: 
    print('Não foi possível realizar o cálculo')