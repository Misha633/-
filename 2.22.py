import sys
print('Добро пожаловать!')
print('Для входа по очереди введите данные:')
v = int(input('Введите свой возраст:   '))
if v <= 17:
    print("Вход воспрещён! Причина - ТЫ ЕЩЁ СЛИШКОМ МАЛЕНЬКИЙ!")
    sys.exit()
    
ima = input('Введите имя:   ')
phm = input('Введите фамилию:   ')

if ima == 'Микордий' and phm == 'Пармезанов':
    print("Вход воспрещён! Причина - Вы находитесь в чёрном списке!")
    sys.exit()
   


print("Хорошего вам вечера!")












