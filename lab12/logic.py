
def validate_records(records):

    if not isinstance(records, list):
        raise ValueError("Корень должен быть списком")
    seen = set()
    for i, r in enumerate(records):
        if not isinstance(r, dict):
            raise ValueError(f"Запись {i}: ожидался объект")
        for key in ("id", "title", "category", "amount", "completed"):
            if key not in r:
                raise ValueError(f"Запись {i}: нет ключа {key}")
        if type(r["id"]) is not int or r["id"] <= 0:
            raise ValueError(f"Запись {i}: id должен быть положительным целым")
        if r["id"] in seen:
            raise ValueError(f"Запись {i}: повторный id {r['id']}")
        seen.add(r["id"])
        if not isinstance(r["title"], str) or not r["title"].strip():
            raise ValueError(f"Запись {i}: title должен быть непустой строкой")
        if not isinstance(r["category"], str) or not r["category"].strip():
            raise ValueError(f"Запись {i}: category должен быть непустой строкой")
        if type(r["amount"]) is not int or r["amount"] < 0:
            raise ValueError(f"Запись {i}: amount должен быть целым >= 0")
        if type(r["completed"]) is not bool:
            raise ValueError(f"Запись {i}: completed должен быть bool")


def add_record(records, title, category, amount):

    title = title.strip()
    category = category.strip()
    if not title:
        raise ValueError("Название не должно быть пустым")
    if not category:
        raise ValueError("Категория не должна быть пустой")
    if type(amount) is not int or amount < 0:
        raise ValueError("Баллы — целое >= 0")
    record = {
        "id": max((r["id"] for r in records), default=0) + 1,
        "title": title,
        "category": category,
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def find_records(records, query):

    q = query.strip().lower()
    if not q:
        raise ValueError("Запрос не должен быть пустым")
    return [r for r in records if q in r["title"].lower()]


def set_completed(records, record_id, completed):

    for r in records:
        if r["id"] == record_id:
            r["completed"] = completed
            return True
    return False


def delete_record(records, record_id):

    for i, r in enumerate(records):
        if r["id"] == record_id:
            del records[i]
            return True
    return False


def statistics(records):

    by_cat = {}
    for r in records:
        key = r["category"].strip()
        by_cat[key] = by_cat.get(key, 0) + r["amount"]
    done = sum(1 for r in records if r["completed"])
    return {
        "total": len(records),
        "completed": done,
        "not_completed": len(records) - done,
        "total_amount": sum(r["amount"] for r in records),
        "by_category": by_cat,
    }