import sys

input = sys.stdin.readline

n = int(input().rstrip())

lst = sorted(list(map(int, input().split())))

x = int(input().rstrip())

cnt = 0
left = 0
right = n-1

while left < right:
    tmp = lst[left] + lst[right]
    if tmp == x:
        cnt += 1
        left += 1
    elif tmp > x:
        right -= 1
    else:
        left += 1

print(cnt)