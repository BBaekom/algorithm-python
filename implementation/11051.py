import sys
input = sys.stdin.readline

N, K = map(int, input().split())

div = 10007

up = down = 1
for i in range(K):
    up = (up * N) % div
    N -= 1

for i in range(K, 1, -1):
    down = (down * i) % div

if K == 0:
    print(1)
else:
    print(up * pow(down, div-2, div) % div)
