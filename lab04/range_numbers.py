
a = int(input())
b = int(input())

if a < b:
    # по возрастанию
    for x in range(a, b + 1):
        print(x)
elif a > b:
    # по убыванию
    for x in range(a, b - 1, -1):
        print(x)
else:
    print(a)