
file = open("1файл.txt", "r", encoding="utf-8")
text1 = int(file.read())
file.close()

file = open("2файл.txt", "r", encoding="utf-8")
text2 = int(file.read())
file.close()

a = text1 + text2



file = open("3файл.txt", "w", encoding="utf-8")
text3 = file.write(str(a))
file.close()










