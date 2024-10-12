
file = open("часть предложения1.txt", "r", encoding="utf-8")
a = file.read()
file = open("часть предложения2.txt", "r", encoding="utf-8")
a1 = file.read()
file = open("часть предложения3.txt", "r", encoding="utf-8")
a2 = file.read()
file = open("часть предложения4.txt", "r", encoding="utf-8")
a3 = file.read()

file = open("готовое предложение.txt", "w", encoding="utf-8")
b = file.write((a + " " + a1 + " " + a2 + " " + a3))
file.close()










