file = open("files1.txt", "r", encoding="utf-8")
text = file.read()
file.close()

file = open("files2.txt", "r", encoding="utf-8")
text1 = file.read()
file.close()
print(text + text1)



















