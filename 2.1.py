print("Выбери один файл из трёх!")
n = int(input())
if n < 1 or n >= 4:
    print("Спасибо за использование!")
    pass


if n == 1:
    file = open("1.txt", "r", encoding="utf-8")
    a = file.read()
    print("В этом файле был", a,":(")
    
if n == 2:
    file = open("2.txt", "r", encoding="utf-8")
    a = file.read()
    print("В этом файле был", a)
    
if n == 3:
    file = open("3.txt", "r", encoding="utf-8")
    a = file.read()
    print("В этом файле был", a) 
    















