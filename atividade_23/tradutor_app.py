'''Crie em Python, um tradutor, e envie o link do repositório.'''
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(souce= 'auto', target = 'pt')

while True:
    texto_usuario = input('Digite o que deseja traduzir, idioma sua escolha: ')
    traducao = tradutor.translate(texto_usuario)

    print(traducao)

    repetir = input('Deseja fazer mais uma tradução (s/n)? ').lower()

    if repetir == 's':
        continue
    else:
        break