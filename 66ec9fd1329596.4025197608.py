"""
Вова узнал про функцию str(), которая преобразует
число в строку, и решил её использовать
для того, чтобы исправить даты в анкетах — там годы начала
и окончания обучения почему-то на 1 больше, чем надо.

Программа должна получить год начала, год получения, увеличить
на 1 и вывести:
Обучался <правильный год начала>-<правильный год окончания> годы
например:
ВВОДИМ:
2003
2007
ПОЛУЧАЕМ:
Обучался 2004-2008 годы

Но программа выдаёт ошибку!

Пожалуйста, минимально изменяйте программу при исправлении, чтобы
не расстраивать Вову.
"""

year1 = int(input("Введите год начала обучения: ")) + 1
year2 = int(input("Введите год окончания обучения: ")) + 1
print("Обучался " + str(year1) + "-" + str(year2) + " годы")
