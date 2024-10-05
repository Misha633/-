file = open("files11.txt", "r", encoding="utf-8")
text = file.read()
file.close()

file = open("files12.txt", "r", encoding="utf-8")
text1 = file.read()
file.close()

file = open("files13.txt", "r", encoding="utf-8")
text2 = file.read()
file.close()

print("Внимание всем!")
print("Потерялся маленький, беззащитный пылесос!")
print("Имя:", text)
print("Предназначение:", text1)
print("Особые приметы:", text2)




