
import json

from logic import validate_records


def load_records(path):

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    validate_records(data)
    return data


def save_records(path, records):
    
    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)