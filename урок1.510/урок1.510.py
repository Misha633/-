file = open("1товар.txt", "r", encoding="utf-8")
a = file.read()
file.close()

print("Я знаю что тебе нужно купить", a, "но запиши второй продукт, который надо купить!")
b = input()
file = open("1товар.txt", "w", encoding="utf-8")
c = file.write((a + " и" + " " + b))
file.close()






