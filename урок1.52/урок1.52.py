file = open("files5.txt", "r", encoding="utf-8")
text = int(file.read())
file.close()

print("Здраствуйте! Я знаю, что у вас есть:", text, "рублей!")
print("Но сколько скажите, пожалуйста, вы заработаете в конце этого месяца?")
zp = int(input())
print("Хорошо, в сумме у вас будет:", text + zp, "рублей!")





