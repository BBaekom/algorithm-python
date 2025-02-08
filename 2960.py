import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def func(n):
    cnt = 0
    res = 0
    arr = [i for i in range(n+1)]
    for i in range(2, n+1):
        if arr[i] == 0:
            continue
        for j in range(i, n+1, i):
            if arr[j] != 0:
                arr[j] = 0
                cnt += 1
                if cnt == K:
                    res = j
    return res

print(func(N))
