import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

def dfs(start):
    dfs_visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not dfs_visited[i]:
            dfs(i)


def bfs(start):
    bfs_visited[start] = True
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if bfs_visited[i] == False:
                bfs_visited[i] = True
                q.append(i)

dfs(V)
print()
bfs(V)