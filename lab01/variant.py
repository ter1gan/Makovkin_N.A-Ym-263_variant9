


order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

# Первая позиция
item1_name = input("Название первой позиции: ")
item1_qty = int(input(f"Количество «{item1_name}»: "))
item1_price = float(input(f"Цена за единицу «{item1_name}»: "))

# Вторая позиция
item2_name = input("Название второй позиции: ")
item2_qty = int(input(f"Количество «{item2_name}»: "))
item2_price = float(input(f"Цена за единицу «{item2_name}»: "))

# Доставка и оплата
delivery = float(input("Стоимость доставки: "))
paid = float(input("Внесённая сумма (руб.): "))

# Расчёты по заказу
item1_cost = item1_qty * item1_price
item2_cost = item2_qty * item2_price
goods_cost = item1_cost + item2_cost
total_with_delivery = goods_cost + delivery
total_qty = item1_qty + item2_qty
change = paid - total_with_delivery

print()
print(f"=== Заказ: {order_name} ===")
print(f"Заказчик: {customer_name}")
print(f"{item1_name} | {item1_qty} | {item1_price:.2f} | {item1_cost:.2f}")
print(f"{item2_name} | {item2_qty} | {item2_price:.2f} | {item2_cost:.2f}")
print(f"Стоимость товаров без доставки: {goods_cost:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Итого с доставкой: {total_with_delivery:.2f} руб.")
print(f"Общее количество единиц: {total_qty}")
print(f"Сдача: {change:.2f} руб.")


print()
#Дополнительно: скидка
discount_percent = float(input("Скидка на товары, % (0-100): "))

discount_amount = goods_cost * discount_percent / 100
discounted_goods = goods_cost - discount_amount
new_total = discounted_goods + delivery
new_change = paid - new_total

print(f"Скидка {discount_percent:.2f}%: {discount_amount:.2f} руб.")
print(f"Новая итоговая сумма (товары со скидкой + доставка): {new_total:.2f} руб.")
print(f"Сдача с учётом скидки: {new_change:.2f} руб.")