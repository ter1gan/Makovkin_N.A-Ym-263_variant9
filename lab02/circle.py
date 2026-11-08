
import math

radius = float(input("Радиус: "))

if radius <= 0:
    print("Ошибка: радиус должен быть положительным.")
    raise SystemExit(1)

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Длина окружности: {circumference:.2f}")
print(f"Площадь круга:    {area:.2f}")