import sys
input = sys.stdin.readline

N  = int(input())

lst = reversed(sorted([int(input()) for _ in range(N)]))

for i in lst:
    print