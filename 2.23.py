import pyautogui
import time
import sys

v = int(input('Здраствуйте! Введите влажность в процентах! '))
t = int(input('Введите температуру в градусах! '))

if v >= 60 and t <= 10 or v <= 30 and t >= 30:
    print("Тревога!!!")
    pyautogui.press('win')
    pyautogui.press('Space')
    pyautogui.write('Chorme')  
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('Xnj ltkfnm ghb yfheitybb eckjdbq d jhty;bhtt?')  
    pyautogui.press('enter')
    sys.exit()
    
    
print("Хорошо!")
    










