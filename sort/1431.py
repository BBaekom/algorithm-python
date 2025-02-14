import sys
input = sys.stdin.readline

N = int(input())

lst = [input().rstrip() for _ in range(N)]
cnt = [0 for _ in range(N)]

def func(a, b):
    tmp = sorted([a, b])
    return tmp[0], tmp[1]


for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j].isdecimal():
            cnt[i] += int(lst[i][j])


for i in range(N-1):
    for j in range(i+1, N):
        if len(lst[i]) > len(lst[j]):
            lst[i], lst[j] = lst[j], lst[i]
            cnt[i], cnt[j] = cnt[j], cnt[i]
        elif len(lst[i]) == len(lst[j]):
            if cnt[i] > cnt[j]:
                lst[i], lst[j] = lst[j], lst[i]
                cnt[i], cnt[j] = cnt[j], cnt[i]
            elif cnt[i] == cnt[j]:
                lst[i], lst[j] = func(lst[i], lst[j])
                
            
for i in lst:
    print(i)