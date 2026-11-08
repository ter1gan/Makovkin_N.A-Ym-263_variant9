
numbers = []
for part in input().split():
    numbers.append(int(part))

selected = []
for value in numbers:
    if value != 0:
        selected.append(value)

count = len(selected)
total = sum(selected)
ordered = sorted(selected)

print(f"Выборка:       {selected}")
print(f"Количество:    {count}")
print(f"Сумма:         {total}")
print(f"По возрастанию: {ordered}")