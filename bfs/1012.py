import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0,0, -1, 1]
    graph[x][y] = 0
    q = deque()
    q.append([x,y])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 0

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    res = 0
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 :
                bfs(i, j)
                res += 1
    print(res)