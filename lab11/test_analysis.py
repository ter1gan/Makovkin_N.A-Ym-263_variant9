import json
from pathlib import Path
from tempfile import TemporaryDirectory

from analysis import (
    completion_counts,
    select_tasks,
    top_users,
    validate_todos,
)

SAMPLE = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]


assert validate_todos(SAMPLE) is True
counts = completion_counts(SAMPLE)
assert counts == {5: 2, 10: 2}
assert top_users(counts) == [5, 10]
leader_ids = [t["id"] for t in SAMPLE if t["userId"] in top_users(counts) and t["completed"]]
assert leader_ids == [1, 3, 4, 5]


assert completion_counts([]) == {}
assert top_users({}) == []
assert select_tasks([], 5, "с") == []


all_false = [
    {"id": 1, "userId": 1, "title": "A", "completed": False},
    {"id": 2, "userId": 2, "title": "B", "completed": False},
]
assert top_users(completion_counts(all_false)) == []


single = [
    {"id": 1, "userId": 1, "title": "A", "completed": True},
    {"id": 2, "userId": 2, "title": "B", "completed": False},
]
assert top_users(completion_counts(single)) == [1]


multi = [
    {"id": 1, "userId": 1, "title": "A", "completed": True},
    {"id": 2, "userId": 2, "title": "B", "completed": True},
    {"id": 3, "userId": 3, "title": "C", "completed": False},
]
assert top_users(completion_counts(multi)) == [1, 2]

#Вариант 9
assert [t["id"] for t in select_tasks(SAMPLE, 5, "с")] == [5]
assert select_tasks(SAMPLE, 999, "с") == []
assert select_tasks(SAMPLE, 10, "х") == []
assert [t["id"] for t in select_tasks(SAMPLE, 5, "С")] == [5]


def expect_value_error(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    assert False, "Ожидалось ValueError"

expect_value_error(validate_todos, {"a": 1})
expect_value_error(validate_todos, [
    {"id": 1, "userId": 1, "title": "A", "completed": True},
    {"id": 1, "userId": 2, "title": "B", "completed": False},
])
expect_value_error(validate_todos, [{"id": 1, "title": "A", "completed": True}])
expect_value_error(validate_todos, [
    {"id": 1, "userId": 1, "title": "A", "completed": "false"},
])
expect_value_error(validate_todos, [
    {"id": True, "userId": 1, "title": "A", "completed": True},
])


with TemporaryDirectory() as directory:
    path = Path(directory) / "selected.json"
    selected = select_tasks(SAMPLE, 5, "с")
    path.write_text(json.dumps(selected, ensure_ascii=False), encoding="utf-8")
    assert json.loads(path.read_text(encoding="utf-8")) == selected

print("Все проверки пройдены")