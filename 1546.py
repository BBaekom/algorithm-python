import sys

input = sys.stdin.readline

N = int(input().rstrip())

arr = list(map(int, input().split()))

M = max(arr)

for i in range(N):
    arr[i] = arr[i] / M * 100

result = sum(arr) / N

print(result)