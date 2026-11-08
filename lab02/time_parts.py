total_seconds = int(input("Введите количество секунд: "))

if total_seconds < 0:
    print("Ошибка: количество секунд не может быть отрицательным.")
    raise SystemExit(1)

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours} ч {minutes} мин {seconds} с")