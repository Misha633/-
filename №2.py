import turtle
turtle.home()
while True:
    a = turtle.textinput('Команда', 'Введите команду:')
    if a == 'Стоп' or a == 'стоп':
        break
    else:
        if type(a) != int:
            a = len(a)
            turtle.forward(a)
        else:
            turtle.forward(a)
            



















