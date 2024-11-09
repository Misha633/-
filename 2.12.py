print("У тебя завтра или после завтра прием у стомотолога?")
p = input()
print("Во сколько, сначало часы, потом минуты?")
pvch = input()
pvm = input()
file = open("zapis.txt", "w", encoding="utf-8")
a = file.write("У тебя " + p + " завтра примем у стомотолога в " + pvch + ":" + pvm)
file.close()












