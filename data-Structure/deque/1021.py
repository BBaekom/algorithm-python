import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# 뽑아내려고 하는 수의 위치 리스트
lst = list(map(int, input().split()))

dq = deque(i for i in range(1, N+1))

cnt = 0

# deque의 index 함수는 dq.index(X)이면 X의 인덱스를 반환해준다.

for i in lst: # 뽑아내야하는 수의 위치 리스트
    while i != dq[0]:
        mid = len(dq) // 2
        if dq.index(i) <= mid:
            dq.rotate(-1)
            cnt += 1
        else:
            dq.rotate(1)
            cnt += 1
    dq.popleft()
    
print(cnt)
            