

def word_counts(text):

    counts = {}
    for raw in text.lower().split():
        word = raw.strip(".,!?;:")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def print_pairs(counts):

    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):

    return sorted(set(first) & set(second))


def all_topics(first, second):

    return sorted(set(first) | set(second))


def totals_by_category(records):

    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):

    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles


def main():
    # Задание 1
    print_pairs(word_counts(input("Текст: ")))

    # Задание 2
    first = input("Темы первого (через пробел): ").split()
    second = input("Темы второго (через пробел): ").split()
    print(f"Общие: {common_topics(first, second)}")
    print(f"Все:   {all_topics(first, second)}")

    # Задание 3
    record = {"title": "Python", "hours": 4}
    record["hours"] = 6
    record["completed"] = False
    pair = (record["title"], record["hours"])
    name, hours = pair
    print(f"Запись: {record}")
    print(f"Пара:   {name}, {hours}")


    tasks = [
        {"title": "Сумма чисел", "category": "базовые", "amount": 10},
        {"title": "Палиндром", "category": "строки", "amount": 15},
        {"title": "Словарь частот", "category": "словари", "amount": 20},
        {"title": "Фильтр списка", "category": "базовые", "amount": 12},
        {"title": "Проверка простоты", "category": "строки", "amount": 25},
    ]
    totals = totals_by_category(tasks)
    for category in sorted(totals):          # сводка по алфавиту
        print(f"{category}: {totals[category]}")
    wanted = input("Категория для поиска: ")
    print(titles_in_category(tasks, wanted))  # неизвестная → []


if __name__ == "__main__":
    main()