# test_collections.py
from collections_lab import (
    all_topics,
    common_topics,
    titles_in_category,
    totals_by_category,
    word_counts,
)

# Задание 1
assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}

# Задание 2
assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
assert all_topics(["python", "sql", "python"], ["sql", "git"]) == ["git", "python", "sql"]


assert common_topics([], ["a", "b"]) == []
assert all_topics([], ["a", "b"]) == ["a", "b"]

# Вариант 9
records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
snapshot = [record.copy() for record in records]

assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []
assert totals_by_category([]) == {}
assert records == snapshot

print("Базовые проверки пройдены")