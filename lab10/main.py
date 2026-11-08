
from pathlib import Path

from files_lab import read_matrix, selected_sum
from table import column_sums, row_sums


def read_positive_integer():

    while True:
        raw = input("Введите целое число > 0: ")
        try:
            number = int(raw)
        except ValueError:
            print("Попробуйте снова")
            continue
        if number <= 0:
            print("Число должно быть больше нуля.")
            continue
        return number


def main():
    folder = Path(__file__).resolve().parent
    source = folder / "matrix.txt"
    target = folder / "report.txt"

    # Задание 1
    demo = read_positive_integer()
    print(f"Получено число: {demo}")

    # Задание 2
    try:
        matrix = read_matrix(source)
    except FileNotFoundError:
        print(f"Файл не найден: {source.name}")
        return
    except UnicodeError as error:
        print(f"Ошибка кодировки файла: {error}")
        return
    except ValueError as error:
        print(f"Ошибка формата: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return

    # Всё проверено — считаем результаты
    rows_total = row_sums(matrix)
    columns_total = column_sums(matrix)
    variant_total = selected_sum(matrix)

    # Задание 3: запись отчёта только после успешной проверки входа
    try:
        with open(target, "w", encoding="utf-8") as file:
            file.write("Суммы строк: " + " ".join(str(v) for v in rows_total) + "\n")
            file.write("Суммы столбцов: " + " ".join(str(v) for v in columns_total) + "\n")
            file.write(f"Результат варианта: {variant_total}\n")
    except OSError as error:
        print(f"Ошибка записи отчёта: {error}")
        return

    print(f"Отчёт записан в {target.name}")


if __name__ == "__main__":
    main()