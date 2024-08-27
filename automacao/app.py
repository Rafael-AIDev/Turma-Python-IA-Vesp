# improta a biblioteca de automação
# NOTE: instale a bibilioteca pyautogui
import pyautogui as auto

# Atrasar os comandos da bibilioteca em meio segundo
auto.PAUSE = 0.5

auto.press('win') # abre p menu iniciar
auto.write('chrome') # digita a palavra "chrome"
auto.press('enter') # aperta enter

# tecla de atalho para maximizar tela
auto.hotkey('alt','space') 
auto.press('x') 

# acesso ao site github
auto.write('github.com') 
auto.press('enter') # aperta enter

# ENTRAR NA PÁGINA DE LOGIN DO GITHUB
for i in range(12):
    auto.press('tab')

auto.press('enter')
