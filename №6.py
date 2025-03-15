


x = 0
arr = ["*", "#", "/", "#", "/", "#","#", "#", "/", "#", "/", "#", "#"] 
while True:
    

    print('Ваше местонахождение: ', arr)
    a = input('Какое действие вы хотите сделать? ')
    
    if x >= 12:
           print('Вы победили!')
           break

    elif a == 'Влево' or a == 'влево':
        if x < 1:
            print('Вы находитесь на краю, двигаться дальше нельзя')
        else:
            arr.pop(x - 1)
            arr.insert(x - 1, '*')
            arr.pop(x)
            arr.insert(x, '#')
            x -= 1
    
    elif a == 'Вправо' or a == 'вправо':
        if x > 7:
            print('Вы находитесь на краю, двигаться дальше нельзя')
        else:
            arr.pop(x + 1)
            arr.insert(x + 1, '*')
            arr.pop(x)
            arr.insert(x, '#')
            x += 1
        
    elif a == 'Прыжок' or a == 'прыжок':
        b = input('Куда вы хотите прыгнуть? ')
        if a == 'Влево' or a == 'влево':
            if x < 2:
                print('Вы находитесь на краю, прыгать дальше нельзя')
            else:
                arr.pop(x - 2)
                arr.insert(x - 2, '*')
                arr.pop(x)
                arr.insert(x, '#')
                x -= 2
        elif a == 'Вправо' or a == 'вправо':
            print()














