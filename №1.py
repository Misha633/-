import turtle
import sys

turtle.home()
while True:
    a = turtle.textinput('Команда', 'Введите команду:')
    if a == 'Стоп' or a == 'стоп':
        break
    elif a == 'Поднять' or a == 'поднять':
        turtle.penup()
    elif a == 'опустить' or a == 'Опустить':
        turtle.pendown()
    elif a == 'Вперед' or a == 'вперед':
        v = turtle.textinput('Введите на сколько шагов вы хотите двинуться вперёд', 'Введите команду:')
        v = int(v)
        turtle.forward(v)
    elif a == 'Назад' or a == 'назад':
        v = turtle.textinput('Введите на сколько шагов вы хотите двинуться назад', 'Введите команду:')
        v = int(v)
        turtle.backward(v)
    elif a == 'Направо' or a == 'направо':
        v = turtle.textinput('Введите на сколько градусов вы хотите повернуться направо', 'Введите команду:')
        v = int(v)
        turtle.right(v)
    elif a == 'Налево' or a == 'налево':
        v = turtle.textinput('Введите на сколько градусов вы хотите повернуться направо', 'Введите команду:')
        v = int(v)
        turtle.left(v)
    elif a == 'толщина' or a == 'Толщина':
        v = turtle.textinput('Назовите толщину своего пера', 'Введите команду:')
        v = int(v)
        turtle.pensize(v)
    elif a == 'Цвет' or a == 'цвет':
        v = turtle.textinput('Назовите цвет своего пера', 'Введите команду:')
        v = int(v)
        turtle.pencolor(v)
    else:
        print('Неизвестная команда, попроуйте ещё раз!')














