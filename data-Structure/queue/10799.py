import sys
input = sys.stdin.readline

lst = [c for c in input().rstrip()]

queue = []

res = 0
cnt_fragile = 0

for i in lst:
    if i == '(':
        queue.append(i)
        cnt_fragile += 1
    elif i == ')':
        if queue[-1] == '(':
            cnt_fragile -= 1
            if cnt_fragile != 0:
                res += cnt_fragile
            queue.append(i)
        else:
            cnt_fragile -= 1
            res += 1
            queue.append(i)

print(res)