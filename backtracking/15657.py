import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))

res = []
def backtrack(n):
    if len(res) == M:
        print(*res)
        return
    for i in range(len(lst)):
        if not lst or n <= i:
            res.append(lst[i])
            backtrack(i)
            res.pop()

backtrack(0)
