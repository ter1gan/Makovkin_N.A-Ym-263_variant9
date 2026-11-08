import json
from pathlib import Path

from analysis import (
    completion_counts,
    select_tasks,
    top_users,
    validate_todos,
)


def read_user_id():

    while True:
        raw = input("user_id (положительное целое): ")
        try:
            value = int(raw)
        except ValueError:
            print("Не целое число. Повторите.")
            continue
        if value <= 0:
            print("Должно быть больше нуля. Повторите.")
            continue
        return value


def read_text_prefix():

    while True:
        text = input("Подстрока для начала названия: ").strip()
        if text:
            return text
        print("Строка не должна быть пустой. Повторите.")


def main():
    folder = Path(__file__).resolve().parent
    source = folder / "todos.json"
    leaders_path = folder / "leaders.json"
    selected_path = folder / "selected.json"

    try:
        with open(source, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл не найден: {source.name}")
        return
    except UnicodeError as error:
        print(f"Ошибка кодировки: {error}")
        return
    except json.JSONDecodeError as error:   # подкласс ValueError — раньше общего
        print(f"Ошибка JSON: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа: {error}")
        return

    try:
        validate_todos(data)
    except ValueError as error:
        print(f"Ошибка структуры: {error}")
        return

    counts = completion_counts(data)
    leaders = top_users(counts)
    leaders_tasks = [
        todo for todo in data
        if todo["userId"] in leaders and todo["completed"]
    ]
    try:
        with open(leaders_path, "w", encoding="utf-8") as file:
            json.dump(leaders_tasks, file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"Ошибка записи leaders.json: {error}")
        return

    user_id = read_user_id()
    prefix = read_text_prefix()
    selected = select_tasks(data, user_id, prefix)

    try:
        with open(selected_path, "w", encoding="utf-8") as file:
            json.dump(selected, file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"Ошибка записи selected.json: {error}")
        return

    print(f"Завершено по пользователям: {counts}")
    print(f"Лидеры: {leaders}")
    print(f"id задач лидеров: {[t['id'] for t in leaders_tasks]}")
    print(f"id выборки: {[t['id'] for t in selected]}")


if __name__ == "__main__":
    main()