
file = open("data0.txt", "r", encoding="utf-8")
r = file.read()
file.close()


for i in range(1, 9):
    print('...')
    file = open(f"data{i}.txt", "w", encoding="utf-8")
    r2 = file.write(r)
    file.close()

















