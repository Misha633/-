print('Ты учишься в Школе №6?')
y = input()
if y == 'да' or y == 'Да':
    print('Ты случайно не в 8 классе?')
    k = input()
else:
    print('Понял, больше не буду тебя беспокоить!')
    if k == 'да' or k == 'Да':
        print('Так... А буква класса не В случайно?!')
        b = input()
    else:
        print('Понял, больше не буду тебя беспокоить!')
        if b == 'да' or b == 'Да':
            print('Хорошо, последний вопрос.')
            print('Не ты ли, случайно Вася Иванов?!!!')
            n = input()
        else:
            print('Понял, больше не буду тебя беспокоить!')
            if n == 'да' or n == 'Да':
                print('А ну стоять...')
                text = pyautogui.alert(text=f'Это ты у меня колпачки на велосипеде скрутил! ТЕБЕ КОНЕЦ!!!', title='...')
            else:
                print('Понял, больше не буду тебя беспокоить!')























