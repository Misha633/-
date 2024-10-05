file = open("files8.txt", "r", encoding="utf-8")
text = file.read()
file.close()

file = open("files9.txt", "r", encoding="utf-8")
text1 = file.read()
file.close()

file = open("files10.txt", "r", encoding="utf-8")
text2 = file.read()
file.close()

print(text, "+", text1, "=", text2)









