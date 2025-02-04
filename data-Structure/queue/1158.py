import sys

input = sys.stdin.readline

N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]
res = []

idx = 0

while lst:
    idx = (idx + (K-1)) % len(lst)
    res.append(lst.pop(idx))
    
print('<' + ", ".join(map(str, res)) + '>')

# 3 6 2 7 5 1 4