file = open("files14.txt", "r", encoding="utf-8")
text = int(file.read())
file.close()

file = open("files15.txt", "r", encoding="utf-8")
text1 = int(file.read())
file.close()

file = open("files16.txt", "r", encoding="utf-8")
text2 = int(file.read())
file.close()

print("Привет, я расчитаю стоимость всех строематерьялов!")
print("При условии, что один крипич стоит 10 рублей, 1 кг цемента- 500 рублей, а 1 кг песка- 200 рублей")
print("Стоимость 200 кирпичей:", text * 200)
print("Стоимость 3 кг цемента:", text1 * 3)
print("Стоимость 5 кг песка:", text2 * 5)
print("И их общая стоимость равняется:", text * 200 + text1 * 3 + text2 * 5, "рублей!")






