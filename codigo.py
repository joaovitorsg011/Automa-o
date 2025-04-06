import pyautogui
from time import sleep
import pandas as pd

tabela = pd.read_csv('produtos.csv')

def acessar_sistema():
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
    pyautogui.press('enter')
    sleep(1)

def fazer_login():
    pyautogui.press('tab')
    sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write('joaovitorsimao13ff@gmail.com')
    pyautogui.press('tab')
    pyautogui.write('30220130Oa?')
    pyautogui.press('tab')
    pyautogui.press('enter')
    sleep(2)

def importar_dados():
    return pd.read_csv('produtos.csv')

import time
import pyautogui

def cadastrar_produto(linha):
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


def cadastrar_todos_produtos(tabela):
    for linha in tabela.itertuples(index=False):
        cadastrar_produto(linha)

def executar_processo():
    acessar_sistema()  
    fazer_login()     
    tabela = importar_dados()  
    cadastrar_todos_produtos(tabela)  

if __name__ == '__main__':
    pyautogui.PAUSE = 1.5 
    executar_processo()
