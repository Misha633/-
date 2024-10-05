file = open("files6.txt", "r", encoding="utf-8")
text = int(file.read())
file.close()

file = open("files7.txt", "r", encoding="utf-8")
text1 = int(file.read())
file.close()

print("Итак, у вас есть", text, "рублей на копилке")
print("Отпуск стоит:", text1, "рублей")
print("По возвращению у вас останется ещё", text - text1, "рублей на копилке!") 













