'''Crie um programa que calcule o IMC do usuário e informe o estado da sua saúde de acordo com seu peso. 
O usuário deverá decidir se de encerrar o programa ou refazer o cálculo. Ao terminar, envie o arquivo .py.'''

# loop
while True:
    nome = input('Informe seu nome: ')
    peso = str(input('Informe seu peso em kg: ')).replace(',', '.')
    altura = str(input('Informe a altura em m em: ')).replace(',', '.')

    #conversão 
    peso = float(peso)
    altura = float(altura)
    # calcula do imc
    imc = peso / (altura ** 2)

    # mostra o valor na tela
    print(f'IMC de {nome}: {imc:,.2f}.')

    # diagnóstico do imc
    if imc <= 16.9:
        print(f'{nome} está muito abaixo do peso.')
        print('Favor procurar um médico urgente.')
    elif imc < 18.5:
        print(f'{nome} está abaixo do peso.')
    elif imc < 25:
        print(f'{nome} está no seu peso ideal.')
    elif imc < 30:
        print(f'{nome} está acima do peso.')
    elif imc < 35:
        print(f'{nome} está com obesidade grau I.')
    elif imc < 40:
        print(f'{nome} está com obesidade grau II.')
    else:
        print(f'{nome} está com obesidade mórbida')
        print('Favor procurar um médico')

    # verifica se o usuário deseja continuar
    continuar = input('Deseja continuar (s/n)? ').lower()
    if continuar == 's':
        continue
    else:
        break
