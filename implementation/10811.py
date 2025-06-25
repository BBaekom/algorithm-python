import sys
input = sys.stdin.readline

N, M  = map(int, input().split())

lst = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    tmp = lst[i-1:j]
    tmp.reverse()
    lst[i-1:j] = tmp

print(*lst, end=" ")