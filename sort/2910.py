import sys
input = sys.stdin.readline

N, C = map(int, input().split())

message = list(map(int, input().split()))

message_cnt = dict()

for i in message:
    if i in message_cnt:
        message_cnt[i] += 1
    else:
        message_cnt[i] = 1

res = sorted(message_cnt.items(), key=lambda x : -x[1])

for cnt in res:
    for _ in range(cnt[1]):
        print(cnt[0], end=' ')