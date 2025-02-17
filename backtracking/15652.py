import sys
input = sys.stdin.readline

N, M = map(int, input().split())

res = []

def func():
    for i in range(1, N+1):
        # 종료 조건
        if len(res) == M:
            print(*res)
            return
        if not res or res[-1] <= i:
            res.append(i)
            func()
            res.pop()

func()