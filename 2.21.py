import time
import pyautogui

print('Привествую! Введите в консоль логин и пароль для входа в файл - "Секретные данные"!')
a = input('Логин:   ')
b = input('Пароль:    ')

if a == 'Пончик' and b == '1234':
    print('Данные верны! Подождите...')
    time.sleep(2)
    pyautogui.keyDown('win')
    pyautogui.press('e')
    pyautogui.keyUp('win')
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    
if a == 'Пончик' and b != '1234':
    print('Пароль неверен!')
    pass

if a != 'Пончик' and b == '1234':
    print('Логин неверен!')
    pass

if a != 'Пончик' and b != '1234':
    print('Логин и пароль неверны!')
    pass
    

    


























