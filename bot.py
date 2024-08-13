import pyautogui
from time import sleep

pyautogui.PAUSE = 1.5
pyautogui.press('win')
pyautogui.write('whats')
pyautogui.press('enter')
sleep(2)
pyautogui.write('Gostosos')
sleep(3)
pyautogui.press('tab')
pyautogui.press('enter')