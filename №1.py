print('Привествую, для входа введите логин и пароль!')
print('Ваш логин?')

a1 = 'wasd'
b1 = 1234

while True:
    a = input()
    if a == a1:
        print('Отлично!')
        while True:
            print('Какой ваш пароль?')
            b = int(input())
            if b == b1:
                print('Вход воспроизведён!!!')
                break
            else:
                print('Попробуйте ещё раз!')
    else:
        print('Поробуйте ещё раз!')
        



















