import sys
input = sys.stdin.readline

N = int(input())

lst = sorted([int(input()) for i in range(N)])

for i in lst:
    print(i)