import sys

input = sys.stdin.readline

N = int(input().rstrip())

arr = []
result = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

for i in range(N):
    cur = arr[i]
    k = 1
    for j in range(N):
        if cur[0] < arr[j][0] and cur[1] < arr[j][1]:
            k += 1
        else:
            continue 
    result.append(k)

print(*result)