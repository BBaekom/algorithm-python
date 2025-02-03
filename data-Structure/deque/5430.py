import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip()) # 테스트 케이스
for _ in range(T):
    p = list(c for c in input().rstrip()) # 명령어 RDD
    n = int(input().rstrip()) # 리스트 내의 수의 개수
    arr = input().rstrip()
    if arr == '[]':
        lst = deque()
    else:
        lst = deque(map(int, arr[1:-1].split(',')))
    # 여기까지 입력
    # 여기서부터 명령어 다시 실행
    flag = True
    cnt = 0
    for cmd in p:
        if cmd == 'R':
            cnt += 1
        else:
            if len(lst) == 0:
                flag = False
                print("error")
                break
            else:
                if cnt%2 == 0:
                    lst.popleft()
                else:
                    lst.pop()
    if flag: 
        if cnt%2 == 1:
            lst.reverse()
            print('[' + ','.join(map(str, lst)) + ']')
        else:
            print('[' + ','.join(map(str, lst)) + ']')