print("Запиши любые два слова!")
a = input()
b = input()
file = open("первый файл.txt", "w", encoding="utf-8")
ima = file.write(a)
file.close()
file = open("второй файл.txt", "w", encoding="utf-8")
ima = file.write(b)
file.close()






