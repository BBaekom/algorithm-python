import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = [i+1 for i in range(N)]

# print(lst)

for _ in range(M):
    i, j = map(int, input().split())
    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]

print(*lst, end=" ")