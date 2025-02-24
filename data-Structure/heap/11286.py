import sys, heapq
input = sys.stdin.readline

N = int(input())
commands = [int(input()) for _ in range(N)]

lst = []
for command in commands:
    if command == 0:
        if not lst:
            print(0)
            continue
        print(heapq.heappop(lst)[1])
    else:
        heapq.heappush(lst, (abs(command), command))