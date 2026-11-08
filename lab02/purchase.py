
price = int(input("Цена одной тетради: "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма: "))

if price < 0 or count < 0:
    print("Ошибка: цена и количество должны быть неотрицательными.")
    raise SystemExit(1)

cost = price * count

if paid < cost:
    print("Ошибка: переданной суммы недостаточно для оплаты.")
    raise SystemExit(1)

change = paid - cost

print(f"Стоимость: {cost}")
print(f"Сдача:     {change}")