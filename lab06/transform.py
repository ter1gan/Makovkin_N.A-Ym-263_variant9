
original = []
for part in input().split():
    original.append(int(part))

transformed = []
for value in original:
    if value < 0:
        transformed.append(-value)
    else:
        transformed.append(value)

print(f"Исходный список: {original}")
print(f"Новый список:    {transformed}")