import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    X = 1
    Y = 0
    for _ in range(N):
        if Y < H:
            Y += 1
        else:
            X += 1
            Y = 1
    if X < 10:
        print(f'{Y}' + '0' + f'{X}')
    else:
        print(f'{Y}' + f'{X}')
                