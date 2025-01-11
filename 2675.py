import sys

input  = sys.stdin.readline

T = int(input())

for _ in range(T):
    r, s = input().split()
    R = int(r)
    S = s.strip()

    result = ""
    for c in S:
        result += c * R

    print(result)