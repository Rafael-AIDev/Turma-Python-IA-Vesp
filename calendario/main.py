# importando biblioteca
import calendar
try: 
    # usuário informa o ano
    ano = int(input('Informe o ano: '))
# exibe o calendario do ano atual

    for mes in range(1, 13):
        print(calendar.month(ano, mes)) 
except:
    print('Não foi possível exibir o calendário.')