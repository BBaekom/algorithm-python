import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range (i-1, j):
        lst[index] = k
    
print(*lst, end=" ")