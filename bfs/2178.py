import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(c for c in map(int, input().rstrip())) for _ in range(N)]

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([x, y])
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]
            if (0 <= new_x < N) and (0 <= new_y < M) and (graph[new_x][new_y] == 1):
                q.append([new_x, new_y])
                graph[new_x][new_y] = graph[cur_x][cur_y] + 1

    return graph[N-1][M-1]

print(bfs(0,0))
    