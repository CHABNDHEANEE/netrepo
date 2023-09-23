number = int(input("Введите номер проездного: "))
print("Результат:")
firstsum = int(number % 10 + number % 100 / 10 + number % 1000 / 100)
secsum = int(number % 10000 / 1000 + number % 100000 / 10000 + number / 100000)
if firstsum == secsum:
    print("Счастливый билет!")
else:
    print("Несчастливый билет")