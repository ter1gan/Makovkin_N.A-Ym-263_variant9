
import json
from pathlib import Path

from logic import (
    add_record, delete_record, find_records, set_completed, statistics,
)
from storage import load_records, save_records


def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Не должно быть пустым.")


def read_int(prompt, minimum):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Нужно целое число.")
            continue
        if value < minimum:
            print(f"Нужно >= {minimum}.")
            continue
        return value


def read_status():
    while True:
        answer = input("Статус (решена/не решена): ").strip().lower()
        if answer == "решена":
            return True
        if answer == "не решена":
            return False
        print("Введите «решена» или «не решена».")


def ask_delete():
    return input("Удалить? (да/нет): ").strip().lower() == "да"


def ask_save():
    while True:
        answer = input("Сохранить перед выходом? (да/нет): ").strip().lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False
        print("Ответьте «да» или «нет».")


def print_records(records, empty_message):
    if not records:
        print(empty_message)
        return
    for r in sorted(records, key=lambda x: x["id"]):
        status = "решена" if r["completed"] else "не решена"
        print(
            f"{r['id']} | {r['title']} | {r['category']} | "
            f"{r['amount']} баллов | {status}"
        )


def print_statistics(records):
    s = statistics(records)
    print(f"Всего: {s['total']} | решено: {s['completed']} | "
          f"не решено: {s['not_completed']}")
    print(f"Сумма баллов: {s['total_amount']}")
    for cat in sorted(s["by_category"]):
        print(f"  {cat}: {s['by_category'][cat]}")


def try_save(path, records):

    try:
        save_records(path, records)
    except OSError as error:
        print(f"Ошибка записи: {error}")
        return False
    print(f"Сохранено: {path.name}")
    return True


def main():
    source = Path(__file__).resolve().parent / "data.json"

    try:
        records = load_records(source)
    except FileNotFoundError:
        records = []
        print(f"{source.name} не найден, начинаем с пустого списка")
    except json.JSONDecodeError as error:
        print(f"Повреждённый JSON: {error}")
        return
    except UnicodeError as error:
        print(f"Ошибка кодировки: {error}")
        return
    except ValueError as error:
        print(f"Неверная структура: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа: {error}")
        return

    while True:
        print("\n1) Показать  2) Добавить  3) Найти  4) Изменить статус")
        print("5) Удалить   6) Статистика 7) Сохранить 8) Выйти")
        command = input("Команда: ").strip()

        if command == "1":
            print_records(records, "Нет записей")
        elif command == "2":
            title = read_non_empty("Название: ")
            category = read_non_empty("Категория: ")
            amount = read_int("Баллы: ", 0)
            add_record(records, title, category, amount)
            print("Добавлено")
        elif command == "3":
            query = input("Подстрока: ").strip()
            try:
                found = find_records(records, query)
            except ValueError as error:
                print(f"Ошибка: {error}")
            else:
                print_records(found, "Ничего не найдено")
        elif command == "4":
            record_id = read_int("ID: ", 1)
            status = read_status()
            if set_completed(records, record_id, status):
                print("Обновлено")
            else:
                print("ID не найден")
        elif command == "5":
            record_id = read_int("ID: ", 1)
            if ask_delete():
                if delete_record(records, record_id):
                    print("Удалено")
                else:
                    print("ID не найден")
            else:
                print("Отменено")
        elif command == "6":
            print_statistics(records)
        elif command == "7":
            try_save(source, records)
        elif command == "8":
            if ask_save():
                if try_save(source, records):
                    break
            else:
                break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()