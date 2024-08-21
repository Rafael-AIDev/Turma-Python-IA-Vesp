# funções 
def mostrar_menu():
    print('1 - Somar')
    print('2 - Subtrair ')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Extrair o resto da divisão')
    print('6 - Potenciação')
    print('Qualquer valor - Sair do programa')

somar           = lambda x,y: x + y
subtrair        = lambda x,y: x - y
multiplicar     = lambda x,y: x * y
dividir         = lambda x,y: x / y
resto           = lambda x,y: x % y
potenciacao     = lambda x,y: x ** y

# programa principal
if __name__ == '__main__':
    while True:
        try:
            mostrar_menu()
            opcao = int(input('Opção desejada: '))
            if opcao > 0 and opcao < 7:
                x = float(input('Informe o valor de x: ').replace(',', '.'))
                y = float(input('Informe o valor de y: ').replace(',', '.'))
                match opcao:
                    case 1:
                        print(f'O valor da soma entre {x} e {y} é {somar(x,y)}.')
                        continue
                    case 2:
                        print(f'O valor da subtração  entre {x} e {y} é {subtrair(x,y)}.')
                        continue
                    case 3:
                        print(f'O valor da multiplição entre {x} e {y} é {multiplicar(x,y)}.')
                        continue
                    case 4:
                        print(f'O valor da divisão entre {x} e {y} é {dividir(x,y)}.')
                        continue
                    case 5:
                        print(f'O resto da divisão entre {x} e {y} é {resto(x,y)}.')
                        continue
                    case 6:
                        print(f'{x} elevado a {y} é {potenciacao(x,y)}.')
                        continue 
                    case _:
                        print('Opção inválida')
                        continue
            else:
                print('Programa encerrado.')
                break
        except:
            print('Não foi possivel verificar a opçãp')
            break        