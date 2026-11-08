surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст: "))
subject = input("Любимый предмет: ")
study_hours = float(input("Часов подготовки в неделю: "))


if not (1 <= age <= 120):
    print("Ошибка: возраст должен быть целым от 1 до 120.")
    raise SystemExit(1)
if study_hours < 0:
    print("Ошибка: количество часов не может быть отрицательным.")
    raise SystemExit(1)

age4 = age + 4
hours4 = study_hours * 4
avg = study_hours / 7

print()

print("КАРТОЧКА СТУДЕНТА")

print(f"Фамилия:                 {surname}")
print(f"Имя:                     {name}")
print(f"Полное имя:              {name} {surname}")
print(f"Группа:                  {group}")
print(f"Город:                   {city}")
print(f"Возраст:                 {age}")
print(f"Возраст через 4 года:    {age4}")
print(f"Любимый предмет:         {subject}")
print(f"Подготовка в неделю:     {study_hours:.2f} ч")
print(f"Подготовка за 4 недели:  {hours4:.2f} ч")
print(f"Среднее в день:          {avg:.2f} ч")
