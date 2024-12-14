import pyautogui

file = open("123.txt", "r", encoding="utf-8")
a = int(file.read())

if a <= 10:
    text = pyautogui.alert(text=f'Принято, ваш вес в {a} кг не привышает нормы!', title='Сообщение')
else:
    text = pyautogui.alert(text=f'Вес слишком большой! Он превышает норму на {a - 10} кг!', title='Сообщение')
    
print('Самолёт вылетает через 2 часа!')










