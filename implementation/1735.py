import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

res1 = A * D + C * B
res2 = B * D

div = gcd(res1, res2)

print(res1 // div, res2 // div)