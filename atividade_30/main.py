'''Crie um programa para automatizar o envio de um programa qualquer para o repositório remoto do GitHub. 
Ao terminar, gere o executável e envie o código-fonte e a pasta do executável.'''
import pyautogui as auto
import time
autoPAUSE = 0.5

auto.press('win')
auto.write('vs')
auto.press('enter')
time.sleep(3)

auto.hotkey('alt', 'space')
auto.press('x')
time.sleep(2)

for i in range(3):
    auto.press('tab')
auto.press('enter')
time.sleep(2)

auto.write('atividade_30')
time.sleep(1)
auto.press('enter')

auto.press('enter')
time.sleep(2)

auto.hotkey('ctrl', 'j')
time.sleep(3)

auto.write('git init')
auto.press('enter')
time.sleep(2)
auto.write('git add .')
auto.press('enter')
time.sleep(2)
auto.write('git commit -m "envio"')
auto.press('enter')
time.sleep(2)
auto.write('git branch -M main')
auto.press('enter')
time.sleep(2)
auto.write('git remote add origin https://github.com/Rafael-AIDev/atividade_30.git')
auto.press('enter')
time.sleep(2)
auto.write('git push -u origin main')
auto.press('enter')