import time

print("Здратсвйте, сейчас я составлю вам анкету!")
name = input("Напишите своё имя ")
otch = input("Напишите своё отчество ")
famil = input("Напишите свою фамилию ")
dspawn = input("Напишите свою дату рождения ")
mspawn = input("Напишите своё место рождения ")
work = input("Напишите через пробел работу и должность ")
print("Отлично! Производится загрузка...")
time.sleep(3)


print("****** АНКЕТА: ******")
print("Имя: ",name)
print("Отчество: ",otch)
print("Фамилия: ",famil)
print("**********")
print("Дата рождения: ",dspawn)
print("Место рождения: ", mspawn)
print("Работа, должность: ", work)
print("**********")







