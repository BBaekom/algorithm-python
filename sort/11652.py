import sys
input = sys.stdin.readline

N = int(input())

num_cnt = dict()

for i in range(N):
    tmp = int(input())
    if tmp in num_cnt:
        num_cnt[tmp] += 1
    else:
        num_cnt[tmp] = 1


num_cnt = sorted(num_cnt.items(), key=lambda x : (-x[1], x[0]))

print(num_cnt[0][0])
