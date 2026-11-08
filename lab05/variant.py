
text = input()

count = 0

for word in text.split():
    cleaned = word.strip(".,!?;:").lower()
    if cleaned == "":
        continue
    if "а" not in cleaned:
        print(cleaned)
        count += 1

if count == 0:
    print("Нет совпадений")

print(f"Количество: {count}")