import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    s = list(input().rstrip())
    flag = False
    n = 0 
    res = 0
    for i in s:
        if i == 'O':
            if flag:
                n += 1
                res += n
            else:
                flag = True
                n = 1 
                res += n
        elif i == 'X':
            flag = False
            continue
    print(res)
                