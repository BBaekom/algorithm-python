import sys, heapq
input = sys.stdin.readline

N = int(input())

lst = [int(input()) for _ in range(N)]

zero_cnt = 0

heap = []
for i in lst:
    if i == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -i)