
a = int(input())
b = int(input())
c = int(input())

if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

print(minimum)