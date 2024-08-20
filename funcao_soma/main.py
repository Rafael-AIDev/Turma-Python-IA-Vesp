# função lambda
somar = lambda x,y: x + y

# programa principal
x = float(input('Informe o valor de x: '))
y = float(input('Informe o valor de y: '))

# exibe o resultado
print(f'A soma de {x} e {y} é {somar(x, y)}.')