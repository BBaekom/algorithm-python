import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    if a == b:
        print(1000 + a * 100)
    else:
        print(1000 + c * 100)
else:
    if c < a and b < a:
        print(a * 100)
    elif c < b and a < b:
        print(b * 100)
    else:
        print(c * 100)
        