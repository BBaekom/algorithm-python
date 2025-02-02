import sys

def gcdlcm(n, m):
    a, b = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = a % b
        a, b = b, t
    result = [a, int(n * m / a)]
    return result


input = sys.stdin.readline

n, m = map(int, input().split())

result = gcdlcm(n, m)

for i in result:
    print(i)