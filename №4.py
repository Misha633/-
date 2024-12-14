import pyautogui

t1 = int(pyautogui.prompt(text='Введите температуру в Антарктиде', title='Датчик №1', default=''))
t2 = int(pyautogui.prompt(text='Введите температуру в Антарктиде', title='Датчик №2', default=''))
t3 = int(pyautogui.prompt(text='Введите температуру в Антарктиде', title='Датчик №3', default=''))

if t1 >= 0 or t2 >= 0 or t3 >= 0:
    print('ОПАСНОСТЬ!!!')
    print("ТАЯНИЕ ЛЬДОВ!")
else:
    print('Температура в норме')




















