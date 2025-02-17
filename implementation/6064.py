import sys
input = sys.stdin.readline

# M, N >= x, y -> <x:y> 각 년도 표시

T = int(input())

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

for _ in range(T):
    M, N, x, y = map(int, input().split())

    last = lcm(M, N)

    a = x

    while a <= last:
        if a % N == y or (y == N and a % N == 0):
            print(a)
            break
        a += M
        if a > last:
            print(-1)
            break
