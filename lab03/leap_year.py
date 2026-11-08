
year = int(input())

if year < 1 or year > 9999:
    print("Ошибка: год вне диапазона 1–9999")
else:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Да, високосный")
    else:
        print("Нет, не високосный")