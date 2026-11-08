

total = int(input("Общее количество билетов: "))
capacity = int(input("Билетов в одной пачке: "))

full_packs = total // capacity
remainder = total % capacity
total_packs = (total + capacity - 1) // capacity

print(f"Полных пачек:    {full_packs}")
print(f"Остаток билетов: {remainder}")
print(f"Всего пачек:     {total_packs}")