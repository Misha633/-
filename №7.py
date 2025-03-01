a = int(input('Введите первое число интервала '))
b = int(input('Введите второе число интервала '))
c = int(input('Введите интервал между числами '))
if a > b > c or b > a > c:
    for i in range(a, b, c):
        print(i)
else:
    print('Неправильно введены данные')
    


















