year = int(input("Введите год: "))
print("Результат:")
if(year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)):
    print("Високосный год")
else:
    print("Обычный год")