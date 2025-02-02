import sys

input = sys.stdin.readline

N = int(input().rstrip())

# 1초 - 2000만 번의 연산
# 조건 : 1초,  n = 100000 -> O(N^2) = 10000000000 -> 100억 번이므로 연산 초과
# O(NlogN) = 100000 * log100000 = 100000 * 16 = 1600000 -> ㄱㄴ!

res = sys.maxsize
tmp = 0


# 최소를 구하라 -> 낮은 수부터 높은수로 찾으면서 가장 먼저 발견되는 수가 최소임!
for i in range(N-1, 0, -1):
    tmp = i
    s = str(i)
    for j in range(len(s)):
        tmp += int(s[j])
    if tmp == N:
        res = min(res, i)

if res == sys.maxsize:
    print(0)
else:
    print(res)