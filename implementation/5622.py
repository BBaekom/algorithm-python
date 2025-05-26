import sys

input = sys.stdin.readline

s = input().rstrip()

telephone = ['1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '0']
res = 0

for i in range(len(s)):
    for j in range(len(telephone)):
        if s[i] in telephone[j]:
            res += j + 2

print(res)