
from functions import (
    average,
    normalize_text,
    select_numbers,
    sum_digits, is_palindrome,
)


def main():

    number = int(input("Целое число: "))
    print(f"Сумма: {sum_digits(number)}")


    numbers = []
    for part in input("Целые числа через пробел: ").split():
        numbers.append(int(part))

    avg = average(numbers)
    if avg is None:
        print("-")
    else:
        print(f"Среднее: {avg:.2f}")


    text = input("Текст: ")
    print(f"Нормализовано: {normalize_text(text)}")


    threshold = int(input("Порог: "))
    selected = select_numbers(numbers, threshold)
    print(f"Выборка от 0 до {threshold}): {selected}")


    candidate = input("Текст для проверки палиндрома: ")
    print(f"Палиндром: {is_palindrome(candidate)}")


if __name__ == "__main__":
    main()