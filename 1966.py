import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # 4 2
    queue = deque(map(int, input().split())) # 1 2 3 4
    idx = deque(i for i in range(N))

    # print(queue)
    # print(idx)
    
    print_cnt = 0
    print_idx = M

    max_num = max(queue) # 4
    while print_idx in idx:
        # pop 하고 다시 max_num 설정
        if queue[0] == max_num:
            queue.popleft()
            idx.popleft()
            print_cnt += 1
            if queue:
                max_num = max(queue)
        else:
            queue.rotate(-1)
            idx.rotate(-1)
    print(print_cnt)