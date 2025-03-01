x = 0
a = int(input('На сколько вы хотите умножить каждое число, получив их сумму в конце? '))
for i in range(0, 100, 2):
    i = i * a
    x = x + i
    print(x)

print(x)















