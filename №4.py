import sys
ch = 12
p = 0
print('Отгадайте число!')
while p < 3:
    a = int(input())
    p += 1
    if a < ch:
        print('Число больше вашего!')
    elif a > ch:
        print('Число меньше вашего!')
    elif a == ch:
        print('Вы угадали!')
        sys.exit()

print('Вы проиграли!!!')











