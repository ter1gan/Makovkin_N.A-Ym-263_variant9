


def validate_todos(data):

    if not isinstance(data, list):
        raise ValueError("Корень должен быть списком")

    seen = set()
    for i, todo in enumerate(data):
        if not isinstance(todo, dict):
            raise ValueError(f"Запись {i}: ожидался объект")

        if "id" not in todo:
            raise ValueError(f"Запись {i}: отсутствует id")
        if type(todo["id"]) is not int or todo["id"] <= 0:
            raise ValueError(f"Запись {i}: id должен быть положительным целым")
        if todo["id"] in seen:
            raise ValueError(f"Запись {i}: повторный id {todo['id']}")
        seen.add(todo["id"])

        if "userId" not in todo:
            raise ValueError(f"Запись {i}: отсутствует userId")
        if type(todo["userId"]) is not int or todo["userId"] <= 0:
            raise ValueError(f"Запись {i}: userId должен быть положительным целым")

        if "title" not in todo:
            raise ValueError(f"Запись {i}: отсутствует title")
        if not isinstance(todo["title"], str) or todo["title"] == "":
            raise ValueError(f"Запись {i}: title должен быть непустой строкой")

        if "completed" not in todo:
            raise ValueError(f"Запись {i}: отсутствует completed")
        if type(todo["completed"]) is not bool:
            raise ValueError(f"Запись {i}: completed должен быть bool")

    return True


def completion_counts(todos):

    counts = {}
    for todo in todos:
        user_id = todo["userId"]
        if user_id not in counts:
            counts[user_id] = 0
        if todo["completed"]:
            counts[user_id] += 1
    return counts


def top_users(counts):

    if not counts:
        return []
    maximum = max(counts.values())
    if maximum == 0:
        return []
    return sorted(user_id for user_id, value in counts.items() if value == maximum)


#Вариант 9

def select_tasks(todos, user_id, parameter=None):

    prefix = parameter.strip().lower() if parameter is not None else None
    result = []
    for todo in todos:
        if todo["userId"] != user_id:
            continue
        if prefix is not None and not todo["title"].lower().startswith(prefix):
            continue
        result.append(todo)
    return result