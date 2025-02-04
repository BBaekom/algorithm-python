import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    L = list(input().rstrip())
    res = []
    tmp = []
    for i in L:
        if i == '<':
            if res:
                tmp.append(res.pop())
        elif i == '>':
            if tmp:
                res.append(tmp.pop())
        elif i == '-':
            if res:
                res.pop()
        else:
            res.append(i)
    res.extend(reversed(tmp))
    print("".join(res))

# B A P C d 