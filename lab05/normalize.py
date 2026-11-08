
original = input()

normalized = " ".join(original.split())

print(f"Исходная длина: {len(original)}")
print(f"Новая длина:    {len(normalized)}")
print(f"Нормализованный текст: {normalized}")
print(f"Слов: {len(normalized.split())}")