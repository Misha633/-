
a = ['яблоко', 'томат', 'ананас', 'апельсин', 'кокос']
v1 = input('На какое слово мне заменить элемент 0 в списке? ')
v2 = input('На какое слово мне заменить элемент 4 в списке? ')

a.pop(0)
a.pop(3)
a.append(v2)
a.insert(0, v1)
print(a)















