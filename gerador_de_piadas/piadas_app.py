# importa bibliotecas
import pyjokes # pip install pyjokes
from deep_translator import GoogleTranslator # pip install deep_translator

tradutor = GoogleTranslator(souce= 'auto', target = 'pt')

while True:
    piada = pyjokes.get_joke()
    piada_traduzida = tradutor.translate(piada)

    print(piada_traduzida)

    repetir = input('Deseja gerar outra piada (s/n)? ').lower()

    if repetir == 's':
        continue
    else: 
        break

