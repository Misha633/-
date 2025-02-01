k = 0
p = 11

file = open("температура.txt", "r", encoding="utf-8")
while p > 0:
    p -= 1
    t = int(file.readline())
    print(t)
    if t > 0:
        k += 1
        
print('Было', k ,'дней со средней температурой выше нуля')
        
    
    
















