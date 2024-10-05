file = open("files3.txt", "r", encoding="utf-8")
text = file.read()
file.close()

file = open("files4.txt", "r", encoding="utf-8")
text1 = file.read()
file.close()

print("Здраствуйте,", text + text1)



















