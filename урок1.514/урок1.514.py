print("Здраствуйте! Я, Поздравлятель!")
print("У вашего друга сегодня день рождение, это значимый празник!")
print("Назовите его имя")
ima = str(input())
print("Сколько лет ему исполняется?")
vozrast = input()
print("За что вы больше всего цените поздравляемого, без «за»?")
cena = str(input())
print("Что вы пожелаете поздравляемому?")
pozelania = str(input())
      
file = open("готовое поздравление.txt", "w", encoding="utf-8")
b = str(file.write("Дорогой" + " " + ima + "!" + " " + "Поздравляем с днём рождения, вот вам и исполнилось" + " " + vozrast + " " + "лет." + " " + "Мы очень ценим вас за" + " " + cena + "." + " " + "Желаем вам" + pozelania + "." + " " + "И ещё раз с днём рождения!"))
file.close()




