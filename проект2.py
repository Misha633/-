import random
import sys
rechka = 1
oruyl = 2
a1 = 0
money = 0

print('Добро пожаловать!')
print('**************************************')
print('Сегодня мы сыграем в монетку')
print('Правила игры: Вы выбираете сторону (орёл или решка), после чего автомат подкидывает монету и провозглашает результат!')
print('Если вы выигрываете - поставленная сумма удваевается, проигываете - сгорает!')
print('**************************************')
file = open("Money.txt", "r", encoding="utf-8")
dengi = int(file.read())
file.close()
while dengi > 0:
    money = dengi
    q = 0
    mmm = input('Сыграем? ')
    print('**************************************')
    if mmm.lower() == 'да':
        print('Запускаю!')
        print('**************************************')
            
        while True:
            r = random.randint(1, 3)
            r == int(r)
            rr = random.randint(rechka, oruyl)
                
            s = int(input('Ваша ставка? '))
            print('**************************************')
            if s > dengi:
                print('Вы хотите поставить больше чем у вас есть, попробуйте заново')
                print('**************************************')
            elif s <= dengi:
                a = input('Какую сторону вы выбираете? ')
                print('**************************************')
                if a == 'Решка' or a == 'решка':
                    a1 = rechka
                    break
                elif a == 'Орел' or a == 'орел':
                    a1 = oruyl
                    break
                else:
                    print('Неверная команда, попробуйте ещё раз!')
                    print('**************************************')
            else:
                print('Неверная команда, попробуйте ещё раз')
                print('**************************************')
                
                    
        if a1 == rr:
            a2 = [1,2]
        else:
            a2 = [0, 3]
            
        if r in a2:
            print('Поздравляю, ты удвоил свой выигрыш!')
            print('**************************************')
            money = money + (s * 2)
            q = 1
            dengi = money
            money = str(money)
            file = open("Money.txt", "w", encoding="utf-8")
            text = file.write(money)
            file.close()
        else:
            print('Ты проиграл!')
            print('**************************************')
            money = money - s
            dengi = money
            money = str(money)
            file = open("Money.txt", "w", encoding="utf-8")
            text = file.write(money)
            file.close()
                
            
    elif mmm == 'Нет' or mmm == 'нет':
       
        print('Результат записан, увидимся!')
        sys.exit()
    else:
        print('Что- то пошло не так, попробуй ещё разок!')
        print('**************************************')
            
        
print('Ой, вы проиграли все свои деньги, вас счёт округлён до 0')
file = open("Money.txt", "w", encoding="utf-8")
dengi = file.write('0')
file.close()



















