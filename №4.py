import turtle
import time
turtle.pensize(10)
file = open("команды tutrtle.txt", "r", encoding="utf-8")
for i in file.readlines():
   
    i = i.replace("\n", '')
    
    time.sleep(1)
    if i == 'идти':
        turtle.forward(10)
    elif i == 'красный':
        turtle.pencolor("red")
    elif i == 'синий':
        turtle.pencolor("blue")
    elif i == 'вправо':
        turtle.right(45)
    elif i == 'толще':
        turtle.pensize(1)














    
file.close()   




