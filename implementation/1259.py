import sys

input = sys.stdin.readline

while (True):
    n = int(input().rstrip())
    if n == 0:
        break
    n = str(n)
    if len(n) == 1:
        print("yes")
        continue
    flag = True
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            flag = False
            break
    if flag:
        print("yes")
    else:
        print("no")