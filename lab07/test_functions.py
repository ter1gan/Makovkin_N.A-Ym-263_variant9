

from functions import (
    average,
    is_palindrome,
    normalize_text,
    select_numbers,
    sum_digits,
)


assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""


assert select_numbers([-5, 0, 2, 5], 2) == [0, 2]


assert select_numbers([], 5) == []


assert select_numbers([-1, 0, 1, 2, 3], 2) == [0, 1, 2]


assert select_numbers([1, 1, 2, 2], 2) == [1, 1, 2, 2]


numbers = [-5, 0, 2, 5]
snapshot = numbers.copy()
select_numbers(numbers, 2)
assert numbers == snapshot


assert is_palindrome("шалаш") is True            # палиндром
assert is_palindrome("пример") is False          # не палиндром
assert is_palindrome("   ") is False             # пустой после очистки

print("Базовые проверки пройдены")