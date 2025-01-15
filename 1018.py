import sys

input = sys.stdin.readline

M, N = map(int, input().split())

board = [list(map(str, input().rstrip())) for _ in range(M)]

res = []

for i in range(N-7):
    for j in range(M-7):
        even_white = 0
        odd_white = 0
        for k in range(i, i+8):
            for h in range(j, j+8):
                if (k+h)%2 == 0: # 짝수
                    if board[h][k] != 'B':
                        even_white += 1
                    elif board[h][k] != 'W':
                        odd_white += 1
                else:
                    if board[h][k] != 'W':
                        even_white += 1
                    elif board[h][k] != 'B':
                        odd_white += 1
        res.append(even_white)
        res.append(odd_white)

print(min(res))