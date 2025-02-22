import sys
from collections import deque
input = sys.stdin.readline

def compare(x, y):
    return (x >= 0 and x < n) and (y >= 0 and y < m)

def bfs(x, y):
    picture[x][y] = 0
    res = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if compare(nx, ny) and picture[nx][ny] == 1:
                picture[nx][ny] = 0
                q.append([nx, ny])
                res += 1
    return res
            

n, m = map(int, input().split())

picture = [list(map(int, input().split())) for _ in range(n)]

cnt = area = 0
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            area = max(bfs(i, j), area)
            cnt += 1
print(cnt)
print(area)
            

