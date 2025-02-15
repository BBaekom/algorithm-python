import sys
input = sys.stdin.readline

T = int(input())    

def func(n, lst):
    start = 0
    end = len(lst) - 1
    idx = 0
    if n <= lst[start]:
        return 0
    while start <= end:
        middle = (start + end) // 2
        if n > lst[middle]:
            idx = middle + 1
            start = middle + 1
        else:
            end = middle - 1
    return idx


for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    res = 0
    for i in range (N):
        res += (func(A[i], B))
    print(res)
    