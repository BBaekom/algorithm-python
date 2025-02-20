import sys
input = sys.stdin.readline

N = int(input())
time = sorted(list(map(int, input().split())))

tmp = 0
sum = 0
for i in time:
    tmp += i
    sum += tmp

print(sum)