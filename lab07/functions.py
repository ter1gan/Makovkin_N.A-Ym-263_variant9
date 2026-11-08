
def sum_digits(number):

    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def average(numbers):

    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):

    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):

    selected = []
    for value in numbers:
        if 0 <= value <= threshold:
            selected.append(value)
    return selected


def is_palindrome(text):

    cleaned = text.lower().replace(" ", "")
    if cleaned == "":
        return False
    return cleaned == cleaned[::-1]