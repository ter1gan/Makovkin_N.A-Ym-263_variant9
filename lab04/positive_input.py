
rejected = 0
value = int(input())

while value <= 0:
    rejected += 1
    value = int(input("Нужно положительноt: "))

print(f"Квадрат: {value * value}")
print(f"Количество попыток: {rejected}")