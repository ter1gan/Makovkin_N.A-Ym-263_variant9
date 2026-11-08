

from pathlib import Path


def read_matrix(path):

    text = Path(path).read_text(encoding="utf-8")  # FileNotFoundError/UnicodeError — наверх

    lines = text.split("\n")

    if lines and lines[-1] == "":
        lines.pop()

    if not lines:
        raise ValueError("Файл пуст")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Строка 1: ожидалось два целых числа — строки и столбцы")
    try:
        rows = int(header[0])
        columns = int(header[1])
    except ValueError:
        raise ValueError("Строка 1: размеры должны быть целыми числами")
    if rows <= 0 or columns <= 0:
        raise ValueError("Строка 1: размеры должны быть положительными")

    data_lines = lines[1:]
    if len(data_lines) != rows:
        raise ValueError(
            f"Ожидалось строк данных: {rows}, получено: {len(data_lines)}"
        )

    matrix = []
    for i, line in enumerate(data_lines, start=2):
        if line == "":
            raise ValueError(f"Строка {i}: пустая строка")
        parts = line.split()
        if len(parts) != columns:
            raise ValueError(f"Строка {i}: ожидалось {columns} чисел")
        try:
            row = [int(part) for part in parts]
        except ValueError:
            raise ValueError(f"Строка {i}: нечисловая ячейка")
        matrix.append(row)
    return matrix


#Вариант 9

def selected_sum(matrix):

    if not matrix:
        return 0
    return sum(matrix[-1])