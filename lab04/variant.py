
n = int(input())

if n < 0:
    print("Ошибка: n должно быть >= 0")
    raise SystemExit(1)

count = 0
total = 0

for i in range(1, n + 1):
    value = int(input())
    if value != 0:
        count += 1
        total += value

print(f"Количество ненулевых: {count}")
print(f"Сумма ненулевых:      {total}")