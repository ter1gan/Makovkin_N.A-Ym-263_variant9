


print("Фрагмент А")


first = "2"
second = "3"
print(f"До преобразования:   first = {first!r} ({type(first).__name__}), "
      f"second = {second!r} ({type(second).__name__})")
first_num = int(first)
second_num = int(second)
print(f"После преобразования: first = {first_num!r} ({type(first_num).__name__}), "
      f"second = {second_num!r} ({type(second_num).__name__})")
print(f"Сумма чисел: {first_num + second_num}")

print()

print("Фрагмент Б")


age_input = input("Возраст: ")
print(f"До преобразования:   age = {age_input!r} ({type(age_input).__name__})")
age = int(age_input)
print(f"После преобразования: age = {age!r} ({type(age).__name__})")
print(f"Возраст через год: {age + 1}")

print()

print("Фрагмент В")


first = 4
second = 7
third = 10
average = (first + second + third) / 3
print(f"Среднее: {average}")