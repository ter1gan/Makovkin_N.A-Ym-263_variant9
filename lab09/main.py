
from table import (
    column_sums,
    diagonal_pattern,
    row_sums,
    transform,
)


def read_matrix():
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    return matrix


def main():
    matrix = read_matrix()

    print(f"Суммы строк:    {row_sums(matrix)}")
    print(f"Суммы столбцов: {column_sums(matrix)}")

    size = int(input("Размер диагонального узора (>= 1): "))
    for row in diagonal_pattern(size):
        print(*row)

    new_matrix = transform(matrix)
    print(f"Исходная таблица:   {matrix}")
    print(f"Новая таблица:      {new_matrix}")


if __name__ == "__main__":
    main()