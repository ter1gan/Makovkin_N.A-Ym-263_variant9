import json
from pathlib import Path
from tempfile import TemporaryDirectory

from storage import load_records, save_records


def expect(fn, *args, exc):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"Ожидалось {exc.__name__}")


with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"
    records = [
        {"id": 1, "title": "Сумма чисел", "category": "базовые", "amount": 10, "completed": True},
        {"id": 2, "title": "Палиндром", "category": "строки", "amount": 15, "completed": False},
    ]

    save_records(path, records)
    assert load_records(path) == records
    assert "Сумма чисел" in path.read_text(encoding="utf-8")

    path.write_text("{ broken", encoding="utf-8")
    expect(load_records, path, exc=json.JSONDecodeError)

    path.write_text('{"a": 1}', encoding="utf-8")
    expect(load_records, path, exc=ValueError)

    path.write_text(json.dumps([
        {"id": 1, "title": "A", "category": "c", "amount": 1, "completed": True},
        {"id": 1, "title": "B", "category": "c", "amount": 1, "completed": False},
    ], ensure_ascii=False), encoding="utf-8")
    expect(load_records, path, exc=ValueError)

    expect(load_records, Path(directory) / "missing.json", exc=FileNotFoundError)

print("test_storage OK")