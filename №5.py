


x = 4
arr = ["#", "#", "#", "#", "*", "#","#", "#", "#"] 
while True:
    
    

    print('Ваше местонахождение: ', arr)
    a = input('Какое действие вы хотите сделать? ')
    
    if a == 'Влево' or a == 'влево':
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
    elif a == 'стоп' or a == 'Стоп':
           print('Вы закончили игру!')
           break
    
    
        
        

        











