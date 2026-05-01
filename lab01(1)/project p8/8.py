pool = "|_1_|_2_|_3_|\n|_4_|_5_|_6_|\n|_7_|_8_|_9_|"
t = True
com1 = ""
com2 = ""
numbers = "123456789"
print(pool)

while t:
   
    x = input("Выберите место куда поставить крестик: ")
    while x not in numbers:
        x = input("Ошибка, выберите место куда поставить крестик: ")
    pool = pool.replace(x, 'x')
    numbers = numbers.replace(x, "")
    print(pool)
    com1 += x
    
    if numbers == "":
        print("Ничья!")
        break
    
    if ("1" in com1 and "2" in com1 and "3" in com1) or \
       ("4" in com1 and "5" in com1 and "6" in com1) or \
       ("7" in com1 and "8" in com1 and "9" in com1) or \
       ("1" in com1 and "4" in com1 and "7" in com1) or \
       ("2" in com1 and "5" in com1 and "8" in com1) or \
       ("3" in com1 and "6" in com1 and "9" in com1) or \
       ("1" in com1 and "5" in com1 and "9" in com1) or \
       ("3" in com1 and "5" in com1 and "7" in com1):
        print("Победа крестиков!")
        break
    
    z = input("Выберите место куда поставить нолик: ")
    while z not in numbers:
        z = input("Ошибка, выберите место куда поставить нолик: ")
    pool = pool.replace(z, 'o')
    numbers = numbers.replace(z, "")
    print(pool)
    com2 += z
    
    if numbers == "":
        print("Ничья!")
        break
    
    if ("1" in com2 and "2" in com2 and "3" in com2) or \
       ("4" in com2 and "5" in com2 and "6" in com2) or \
       ("7" in com2 and "8" in com2 and "9" in com2) or \
       ("1" in com2 and "4" in com2 and "7" in com2) or \
       ("2" in com2 and "5" in com2 and "8" in com2) or \
       ("3" in com2 and "6" in com2 and "9" in com2) or \
       ("1" in com2 and "5" in com2 and "9" in com2) or \
       ("3" in com2 and "5" in com2 and "7" in com2):
        print("Победа ноликов!")
        break