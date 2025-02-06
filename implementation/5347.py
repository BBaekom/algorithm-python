import sys
input = sys.stdin.readline

T = int(input())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a < b:
        a, b = b, a
    return a * b / gcd(a, b)

for _ in range(T):
    a, b = map(int, input().split())
    print(round(lcm(a, b)))