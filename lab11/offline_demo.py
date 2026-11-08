import json
from pathlib import Path

path = Path(__file__).resolve().parent / "profile_sample.json"
with open(path, "r", encoding="utf-8") as file:
    data = json.load(file)

print(f"Логин (локальный пример): {data['login']}")