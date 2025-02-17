import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 4, 2

lst = sorted(list(map(int, input().split()))) # N개의 수

res = []

def func():
    if len(res) == M:
        print(*res)
        return
    for i in range(len(lst)):
        if lst[i] in res:
            continue
        res.append(lst[i])
        func()
        res.pop()

func()