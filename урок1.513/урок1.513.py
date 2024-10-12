file = open("первое число.txt", "r", encoding="utf-8")
a = int(file.read())
file.close()

print("Я знаю ваше число, и оно является:", a)
print("Введите второе число")
b = int(input())
c = str(a + b)
file = open("сумма.txt", "w", encoding="utf-8")
b = file.write(c)
file.close()
print("Теперь сумма чисел в вашем файле!")



