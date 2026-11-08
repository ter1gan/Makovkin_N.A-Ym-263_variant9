subject1 = input("Название первого предмета: ")
count1 = int(input(f"Количество занятий по {subject1} за неделю: "))
duration1 = int(input(f"Продолжительность занятия {subject1} (мин): "))

subject2 = input("Название второго предмета: ")
count2 = int(input(f"Количество занятий по {subject2} за неделю: "))
duration2 = int(input(f"Продолжительность занятия {subject2} (мин): "))

available_hours = float(input("Доступное время на неделю (ч): "))


if count1 < 0 or count2 < 0:
    print("Ошибка: количество занятий не может быть отрицательным.")
    raise SystemExit(1)
if duration1 <= 0 or duration2 <= 0:
    print("Ошибка: продолжительность занятия должна быть положительной.")
    raise SystemExit(1)

minutes1 = count1 * duration1
minutes2 = count2 * duration2
total_minutes = minutes1 + minutes2
total_hours = total_minutes / 60

if available_hours < total_hours:
    print("Ошибка: доступное время меньше суммарной нагрузки.")
    raise SystemExit(1)

remaining_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4

print()

print("УЧЕБНАЯ НАГРУЗКА")

print(f"{subject1}: {minutes1} мин")
print(f"{subject2}: {minutes2} мин")
print(f"Общая нагрузка: {total_minutes} мин = {total_hours:.2f} ч")
print(f"Остаток свободного времени: {remaining_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {four_weeks_hours:.2f} ч")

