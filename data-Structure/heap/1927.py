import sys
import heapq
input = sys.stdin.readline

N = int(input())

command = [int(input()) for _ in range(N)]
lst = []
for c in command:
    if c == 0:
        if not lst:
            print(0)
        else:
            print(heapq.heappop(lst))
    else:
        heapq.heappush(lst, c)