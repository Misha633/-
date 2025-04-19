import random
import sys
rechka = 1
oruyl = 2
a1 = 0
money = 0

print('Добро пожаловать!')
print('Сегодня мы сыграем в монетку')
print('Правила игры: Вы выбираете сторону (орёл или решка), после чего автомат подкидывает монету и провозглашает результат!')
print('Если вы выигрываете - поставленная сумма удваевается, проигываете - сгорает!')
file = open("Money.txt", "r", encoding="utf-8")
dengi = int(file.read())
file.close()
while dengi > 0:
    money == dengi
    mmm = input('Сыграем? ') 
    if mmm == 'Да' or mmm == 'да':
        print('Запускаю!')
            
        while True:
            r = random.randint(1, 3)
            r == int(r)
            rr = random.randint(rechka, oruyl)
                
            s = int(input('Ваша ставка? '))
            if s > dengi:
                print('Вы хотите поставить больше чем у вас есть, попробуйте заново')
            elif s <= dengi:
                a = input('Какую сторону вы выбираете? ')
                if a == 'Решка' or a == 'решка':
                    a1 = rechka
                    break
                elif a == 'Орел' or a == 'орел':
                    a1 = oruyl
                    break
                else:
                    print('Неверная команда, попробуйте ещё раз!')
            else:
                print('Неверная команда, попробуйте ещё раз')
                
                    
        if a1 == rr:
            a2 = [1,2]
        else:
            a2 = [0, 3]
            
        for i in a2:
            if i == r:
                print('Поздравляю, ты удвоил свой выигрыш!')
                money = money * 2
                    
        if a2 != r:
            print('Ты проиграл!')
            money = money - s
                
            
    elif mmm == 'Нет' or mmm == 'нет':
        
        file = open("Money.txt", "w", encoding="utf-8")
        dengi = file.write(money)
        file.close() 
        print('Результат записан, увидимся!')
        sys.exit()
    else:
        print('Что- то пошло не так, попробуй ещё разок!')
            
        
print('Ой, вы проиграли все свои деньги, вас счёт округлён до 0')
file = open("Money.txt", "w", encoding="utf-8")
dengi = file.write('0')
file.close()

















