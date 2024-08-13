# Passo 1 = Entrar no sistema da empresa
    #Link = https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 = Fazer login
# Passo 3 = Importar a base de dados
# Passo 4 = Cadastrar um produto
# Passo 5 = Repetir o passo 4 ate cadastrar todos produtos
    
import pyautogui
from time import sleep
# pyautogui.click - clicar com mouse
# pyautogui.write - escrever texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinacoes de teclas
# pyautogui.scroll - rolar a tela
pyautogui.PAUSE = 1.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
sleep(2.5)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(3.5)
pyautogui.press('tab')
sleep(2.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('joaovitorsimao13ff@gmail.com')
pyautogui.press(('tab'))
pyautogui.write('30220130Oa?')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(3.5)


import pandas

tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.click(x=1002, y=191)

