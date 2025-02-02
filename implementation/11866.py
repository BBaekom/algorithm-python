# % 연산을 통해 index를 되돌리는 방법을 잘 익혀야함

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

result = []
lst = [i for i in range(1, N + 1)]

idx = 0

while len(lst) != 0:
    idx += K - 1
    if idx >= len(lst):
        idx %= len(lst)
    result.append(lst.pop(idx))

print('<', end="")
for i in result:
    if i == result[-1]:
        print(i, end="")
    else:
        print(i, end=", ")
print('>', end="")
