import sys
input = sys.stdin.readline

N = int(input().rstrip())

outline = 2 * N - 1

for i in range(1, outline + 1):
    if i <= N:
        print(" " * (N-i), end="")
        print("*" * (2*i - 1), end="\n")
    else:
        print(" " * (i-N), end="")
        print("*" * (2 * (outline-i) + 1), end="\n")
    