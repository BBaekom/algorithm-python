import sys

input = sys.stdin.readline

N = int(input().rstrip())

dis = 1

room = 1

while room < N:
    room = room + (dis * 6)
    dis += 1

print(dis)