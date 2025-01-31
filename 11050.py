import sys

input = sys.stdin.readline

N, K = map(int, input().split())

tmp1 = 1
tmp2 = 1

for i in range(K):
    tmp1 *= N
    N = N-1

for i in range(K, 0, -1):
    tmp2 *= i

result = tmp1 // tmp2
print(result)