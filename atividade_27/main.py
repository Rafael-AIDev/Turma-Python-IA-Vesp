'''Crie um programa que receba do usuário um número inteiro positivo, e o programa retorne a quantidade de números informada da sequência de Fibonacci.'''

# função recursiva de Fibonacci
def calcular_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)
    
# programa principal
n = int(input('Informe o número de sequências a ser calculada: '))

# exibe a sequência 
for x in range(n):
    print(calcular_fibonacci(x))