file = open("1\data.txt", "r", encoding="utf-8")
r = file.read()
file.close()


for i in range(1, 11):
    print('...')
    file = open(f"{i}\data.txt", "w", encoding="utf-8")
    r2 = file.write(r)
    file.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    