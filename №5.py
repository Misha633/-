import pyautogui

print('Здраствуйте!')
while True:
    print('Введите команду!')
    a = input()
    if a == 'стоп' or a == 'Стоп':
        print('Программа остановлена!')
        break
    elif a == 'Открыть' or a == 'открыть':
        print('Для открытия нужного файла напишите его название (с расширением)')
        name = input()
        pyautogui.hotkey('win', 'r')
        pyautogui.hotkey('ctrl', 'v')
    elif a == 'Заменить' or a == 'заменить':
        a1 = input('Введите название файла ')
        text0 = input('Какой текст вы хотите написать? ')
        file = open(a1, "w", encoding="utf-8")
        text = file.write(text0)
        file.close()

    elif a == 'Добавить' or a == 'добавить':
        a2 = input('Введите название файла ')
        text1 = input('Какой текст вы хотите написать? ')
        file = open(a2, "a", encoding="utf-8")
        text = file.write(' ' + text1)
        file.close()
        
    elif a == 'показать' or a == 'Показать':
        a3 = input('Введите название файла ')
        file = open(a3, "r", encoding="utf-8")
        text = file.read()
        file.close()
        print('Текст в файле: ', text)
    elif a == 'создать' or a == 'Создать':




















