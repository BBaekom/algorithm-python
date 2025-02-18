import sys
input = sys.stdin.readline

N, K = map(int, input().split())

div = 10007

up = down = 1
for i in range(K):
    up *= N
    N -= 1

for i in range(K, 1, -1):
    down *= i

if K == 0:
    print(1)
else:
    print((up // down) % div)
