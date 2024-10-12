
file = open("исходник1.txt", "r", encoding="utf-8")
a = file.read()
file.close()
file = open("копирование1.txt", "w", encoding="utf-8")
b = file.write(a)
file.close()





