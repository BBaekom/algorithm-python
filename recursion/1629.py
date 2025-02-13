import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def func(n):
    global A, C
    if n == 1:
        return A % C
    else:
        tmp = func(n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * A) % C

res = func(B)
print(res)

