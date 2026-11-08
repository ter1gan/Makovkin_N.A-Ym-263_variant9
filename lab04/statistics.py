
n = int(input())

if n < 1:
    print("Ошибка: n должно быть >= 1")
    raise SystemExit(1)

first = int(input())
total = first
maximum = first
positive = 1 if first > 0 else 0

for i in range(2, n + 1):
    value = int(input())
    total += value
    if value > maximum:
        maximum = value
    if value > 0:
        positive += 1

print(f"Сумма:           {total}")
print(f"Положительных:   {positive}")
print(f"Максимум:        {maximum}")