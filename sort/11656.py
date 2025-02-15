import sys
input = sys.stdin.readline

S = input().rstrip()

res = []

for i in range(len(S)):
    res.append(S[i:])

for i in sorted(res):
    print(i)