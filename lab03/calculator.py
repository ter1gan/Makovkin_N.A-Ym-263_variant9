
a = float(input())
op = input()
b = float(input())

if op == "+":
    result = a + b
    print(f"{result:.2f}")
elif op == "-":
    result = a - b
    print(f"{result:.2f}")
elif op == "*":
    result = a * b
    print(f"{result:.2f}")
elif op == "/":

        result = a / b
        print(f"{result:.2f}")
else:
    print("Неизвестная операция")