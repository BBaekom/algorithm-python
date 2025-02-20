import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = sorted(list(map(int, input().split()))) # 9 8 7 1 -> 1 7 8 9

res = []
def func():
    if len(res) == M:
        print(*res)
        return
    else:
        for i in lst:
            res.append(i)
            func()
            res.pop()

func()