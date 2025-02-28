import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(N))

idx = deque()
non_zero = True
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            idx.append((i, j))
        elif graph[i][j] == 0:
            non_zero = False

def bfs():
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while idx:
        x, y = idx.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                idx.append((nx, ny))

if non_zero:
    print(0)
else:
    res = 0
    bfs()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                print(-1)
                exit(0)
            res = max(res, graph[i][j])
    print(res - 1)

# 아이디어 : 1인 칸의 index를 모두 저장 -> index 마다 상하좌우 한 번씩 탐색하는 
# bfs를 실행하고