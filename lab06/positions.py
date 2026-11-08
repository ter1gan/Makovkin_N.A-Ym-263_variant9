
numbers = []
for part in input().split():
    numbers.append(int(part))

if not numbers:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []
    for index, value in enumerate(numbers):
        if value == maximum:
            positions.append(index)
    print(positions)