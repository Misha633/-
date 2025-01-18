print('Введите любое слово для добавления его в словарь!')
print('Для остановки напишите "стоп"')
while True:
    a = input('Какое слово ввести? ')
    if a != 'стоп':
        file = open("Словарь.txt", "a", encoding="utf-8")
        text = file.write(a + '\n')
        file.close()
    elif a == 'стоп':
        print('Программа прекратила работу')
        break
    






















