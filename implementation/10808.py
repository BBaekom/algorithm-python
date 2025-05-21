import sys

input = sys.stdin.readline

S = input().rstrip()

# 97 ~ 122 : a ~ z
alp = [0 for _ in range(26)]

for c in S:
    alp[ord(c) - 97] += 1

print(*alp, end=" ")
    
