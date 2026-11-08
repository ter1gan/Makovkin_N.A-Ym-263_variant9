
from table import (
    column_sums,
    diagonal_pattern,
    row_sums,
    transform,
)

# Прямоугольная 2×3
assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
assert column_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]

# Один элемент
assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

# Один столбец, три строки
assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]

# Пустая матрица
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

# Узор размера 3
assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0],
]

# Вариант 9
control = [[-2, 0, 3], [4, -5, 6]]
assert transform(control) == [[-2, 3, 3], [4, -5, 3]]


snapshot = [row.copy() for row in control]
result = transform(control)
result[0][0] = 999
assert control == snapshot

print("Базовые проверки пройдены")