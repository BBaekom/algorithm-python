import sys

input = sys.stdin.readline

alpha = [chr(c) for c in range(97, 123)]
arr = [-1] * 26

S = list(input().rstrip())

for i in range(len(S)):
    for j in range(len(alpha)):
        if S[i] == alpha[j] and arr[j] == -1:
            arr[j] = i

for c in arr:
    print(c, end=" ")