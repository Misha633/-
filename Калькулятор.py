

print('Добро пожаловать в калькулятор!')
print('Введите две первых английских буквы, какой арифметический оператор вы хотите использовать?')
print('+, -, * или / = pl, mi, mu или sp')
op = input(': ')
print('Отлично, выберите два числа с которыми хотите производить действие!')
ch1 = int(input(': '))
ch2 = int(input(': '))

a = ch1 + ch2
b = ch1 - ch2
c = ch1 * ch2
d = ch1 / ch2

s1 = str(a)
s2 = str(b)
s3 = str(c)
s4 = str(d)
s = str(ch1)
st = str(ch2)
if op == 'pl':
    print('Сумма ваших чисел: ', ch1 + ch2)
    file = open("История вычислений.txt", "a", encoding="utf-8")
    b = file.write(s + ' + ' + st + '= ' + s1 + '\n')
    file.close()
if op == 'mi':
    print('Разность ваших чисел: ', ch1 - ch2)
    file = open("История вычислений.txt", "a", encoding="utf-8")
    b = file.write(s + ' - ' + st + '= ' + s2 + '\n')
    file.close()
if op == 'mu':
    print('Произведение ваших чисел: ', ch1 * ch2)
    file = open("История вычислений.txt", "a", encoding="utf-8")
    b = file.write(s + ' * ' + st + '= ' + s3 + '\n')
    file.close()
if op == 'sp':
    print('Частное ваших чисел: ', ch1 / ch2)
    file = open("История вычислений.txt", "a", encoding="utf-8")
    b = file.write(s + ' / ' + st + '= ' + s4 + '\n')
    file.close()
    
print('Ваш пример автоматически сохранился в текстовом файле! Вы всегда можете почистить файл в ручную.')
pass

















