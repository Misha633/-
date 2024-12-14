import pyautogui
import time

print('Здраствуйте введите логин и пароль...')
time.sleep(1)
text = pyautogui.prompt(text='Введите ваш логин:', title='Защитник', default='')
text1 = pyautogui.prompt(text='Введите ваш пароль:', title='Защитник', default='')
if text == 'Misha123' and text1 == '12345':
    print('«Добро пожаловать,', text, '!')
else:
    print('Логин или пароль неверен!')
print('Спасибо, что пользуетесь технологиями Umbrella Corporation!')





























