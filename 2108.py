import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = [int(input()) for i in range(N)]

# 산술평균
print(round(sum(lst) / N))

# 중앙값
lst.sort()
print(lst[N//2])

dic = dict()
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# 최빈값
cnt = []
m = max(dic.values())
for i in dic:
    if dic[i] == m:
        cnt.append(i)

if len(cnt) > 1:
    print(cnt[1])
else:
    print(cnt[0])

# 범위
print(max(lst) - min(lst))

