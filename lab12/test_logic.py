from logic import (
    add_record, delete_record, find_records, set_completed,
    statistics, validate_records,
)


def sample():
    return [
        {"id": 1, "title": "Сумма чисел", "category": "базовые", "amount": 10, "completed": True},
        {"id": 2, "title": "Палиндром", "category": "строки", "amount": 15, "completed": False},
        {"id": 3, "title": "Словарь частот", "category": "словари", "amount": 20, "completed": True},
    ]


def fail(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError("Ожидалось ValueError")


# Проверка структуры
validate_records([])
validate_records(sample())
fail(validate_records, {})
fail(validate_records, [{"id": 1, "title": "A", "category": "c", "amount": 1, "completed": True},
                        {"id": 1, "title": "B", "category": "c", "amount": 1, "completed": False}])
fail(validate_records, [{"id": 1, "title": "  ", "category": "c", "amount": 1, "completed": True}])
fail(validate_records, [{"id": 1, "title": "A", "category": "c", "amount": -1, "completed": True}])
fail(validate_records, [{"id": 1, "title": "A", "category": "c", "amount": True, "completed": True}])
fail(validate_records, [{"id": True, "title": "A", "category": "c", "amount": 1, "completed": True}])
fail(validate_records, [{"id": 1, "title": "A", "category": "c", "amount": 1, "completed": "false"}])

# add_record
empty = []
first = add_record(empty, "Задача", "категория", 5)
assert first["id"] == 1 and first["completed"] is False
assert empty == [first]

trim = []
add_record(trim, "  Python  ", "  учёба  ", 3)
assert trim[0]["title"] == "Python" and trim[0]["category"] == "учёба"

records = sample()
add_record(records, "Новая", "категория", 7)
assert records[-1]["id"] == 4

dup = []
add_record(dup, "Дубликат", "c", 1)
add_record(dup, "Дубликат", "c", 1)
assert len(dup) == 2 and dup[0]["id"] != dup[1]["id"]

fail(add_record, [], "   ", "c", 1)
fail(add_record, [], "t", "   ", 1)
fail(add_record, [], "t", "c", -1)

# find_records — без учёта регистра, список не меняется
records = sample()
found = find_records(records, "ПАЛИ")
assert [r["id"] for r in found] == [2]
before = [r.copy() for r in records]
find_records(records, "а")
assert records == before
fail(find_records, records, "   ")

# set_completed
records = sample()
assert set_completed(records, 2, True) is True
assert records[1]["completed"] is True
before = [r.copy() for r in records]
assert set_completed(records, 999, True) is False
assert records == before

# delete_record + новин id после удаления
records = sample()
delete_record(records, 1)
add_record(records, "Новая", "c", 1)
assert records[-1]["id"] == 4      # max был 3

# статистика по двум категориям
two_cat = [
    {"id": 1, "title": "A", "category": "базовые", "amount": 10, "completed": True},
    {"id": 2, "title": "B", "category": "строки", "amount": 5, "completed": False},
    {"id": 3, "title": "C", "category": "базовые", "amount": 3, "completed": True},
]
s = statistics(two_cat)
assert (s["total"], s["completed"], s["not_completed"], s["total_amount"]) == (3, 2, 1, 18)
assert s["by_category"] == {"базовые": 13, "строки": 5}

# пустой список
s = statistics([])
assert s == {"total": 0, "completed": 0, "not_completed": 0,
             "total_amount": 0, "by_category": {}}

print("test_logic OK")