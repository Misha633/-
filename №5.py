import random
pb0 = 0
pr0 = 0

file = open("Победы.txt", "r", encoding="utf-8")
for pb in file.readlines(): 
    pb0 += 1
file.close()

file = open("Поражения.txt", "r", encoding="utf-8")
for pr in file.readlines():
    pr0 += 1
file.close()

s = 0
ehp = 20
php = 20

print('Победы:', pb0 , 'Поражения:', pr0)
for iii in 1,2,3,4,5,6,7,8,9,10:
    s += 1
    print('Ход номер', s)
    d = input('Выберите действие! (Атака или Защита) ')
    if d == 'атака' or d == 'Атака':
        a = random.randint(1,6)
        if a == 1:
            print('Вы получили урон в 5 здоровья!')
            php -= 5
        elif a == 2 or a == 3:
            print('Вы получил урон в 3 здоровья')
            php -= 3
        elif a == 4 or a == 5:
            print('Вы нанесли 3 урона')
            ehp -= 3
        elif a == 6:
            print('Вы нанесли 5 урона')
            ehp -= 5
    elif d == 'защита' or d == 'Защита':
        b = random.randint(1,6)
        if b == 6:
            print('Вы востановили 5 здоровья')
            php += 5
        elif b == 5 or b == 4:
            print('Вы востановили 1 здоровьe')
            php += 1
        elif b == 3 or b == 2:
            print('Вы ничего не смогли сделать')
        elif b == 1:
            print('Вам пробили броню и нанесли 2 урона')
            php -= 2
    print('Ваше хп:', php, 'Хп противника:', ehp)
                
    if php > 20:
        print('Ваше здоровье достигло максимального значения, оно не может быть выше 20!')
        php = php - (php - 20)
   
    if php <= 0:
        print('Вы проиграли!')
        file = open("Поражения.txt", "w", encoding="utf-8")
        x = file.write(1)
        file.close()
    elif ehp <= 0:
        print('Вы победили!')
        file = open("Победы.txt", "w", encoding="utf-8")
        x = file.write(1)
        file.close()
    
                
        
                


















