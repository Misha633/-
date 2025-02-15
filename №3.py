g = 1000


file = open("Грузы в контейнерах.txt", "r", encoding="utf-8")
for a in file.readlines():
    a = int(a)
    print('Вес груза: ', a)
    if a >= g:
        print('Слишком тяжело!')
    else:
        print('Принято!')
    
    
file.close()   

















