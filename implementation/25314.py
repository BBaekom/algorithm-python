import sys

input = sys.stdin.readline

N = int(input().rstrip())

for _ in range(N//4):
    print("long", end=" ")

print("int")