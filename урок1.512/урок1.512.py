file = open("кол-во запусков.txt", "r", encoding="utf-8")
kolvo = int(file.read())
file.close()
print("Привет, я буду считать запуски этой программы!")
file = open("кол-во запусков.txt", "w", encoding="utf-8")
a = file.write(str(kolvo + 1))
file.close()





