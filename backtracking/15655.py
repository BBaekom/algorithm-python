import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = sorted(list(map(int, input().split())))

res = []

idx = 0

def func():
    if len(res) == M:
        print(*res)
        return
    for i in lst:
        if not res or res[-1] < i:
            res.append(i)
            func()
            res.pop()

func()