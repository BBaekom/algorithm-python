import sys

input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int,input().split()))

res = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tmp = card[i] + card[j] + card[k]
            if tmp >= res and tmp <= M:
                res = tmp
            else:
                continue

print(res)