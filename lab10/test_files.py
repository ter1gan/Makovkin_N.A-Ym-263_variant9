
from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import read_matrix


def expect_value_error(path, fragment=""):
    try:
        read_matrix(path)
    except ValueError as error:
        if fragment:
            assert fragment in str(error), f"Нет «{fragment}» в «{error}»"
    else:
        assert False, "Ошибка не обнаружена"


with TemporaryDirectory() as directory:
    folder = Path(directory)


    path = folder / "matrix.txt"
    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]


    path = folder / "one.txt"
    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]


    path = folder / "empty.txt"
    path.write_text("", encoding="utf-8")
    expect_value_error(path)


    path = folder / "zero.txt"
    path.write_text("0 3\n", encoding="utf-8")
    expect_value_error(path)


    path = folder / "short.txt"
    path.write_text("1 2\n1\n", encoding="utf-8")
    expect_value_error(path, "Строка 2")


    path = folder / "x.txt"
    path.write_text("1 2\n1 x\n", encoding="utf-8")
    expect_value_error(path, "Строка 2")


    path = folder / "extra.txt"
    path.write_text("1 1\n0\n1\n", encoding="utf-8")
    expect_value_error(path)


    missing = folder / "missing.txt"
    try:
        read_matrix(missing)
    except FileNotFoundError:
        pass
    else:
        assert False, "FileNotFoundError не вызван"

print("Все проверки пройдены")