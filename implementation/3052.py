import sys

input = sys.stdin.readline

l = []

for _ in range(10):
    n = int(input())
    l.append(n%42)

s = set(l)
print(len(s))