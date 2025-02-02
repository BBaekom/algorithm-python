import sys

input = sys.stdin.readline

K = int(input().rstrip())

lst = []

for i in range(K):
    tmp = int(input().rstrip())
    if tmp == 0:
        lst.pop(-1)
    else:
        lst.append(tmp)
    
print(sum(lst))