print("Привет, напиши свое имя!")
a = input()
print("Хорошо, а теперь фамилию")
b = input()

file = open("Имя и фамилия1.txt", "w", encoding="utf-8")
ima = file.write((a + " " + b))
file.close()




