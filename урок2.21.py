print("Введите температуру в градусах!")
c = int(input())
if c > 25:
    print("Слишком жарко! Оптимальная температура на", c - 25, "холоднее. Включаю кондиционер. Сейчас станет прохладнее.")
if c < 20:
    print("Слишком холодно! Оптимальная температура на", 20 - c,"теплее. Включаю обогреватель. Сейчас станет теплее.")
if c > 19 and c < 26:
    print("Всё отлично!")

print("Хорошего отдыха!")
