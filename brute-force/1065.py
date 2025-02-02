import sys

sys.stdin.readline

N = int(input().rstrip())

lst_sum = 0

for i in range(1, N+1):
    tmp = str(i)
    if len(tmp) == 1:
        lst_sum += 1
    else:
        flag = True
        sub = int(tmp[1]) - int(tmp[0])
        for j in range(len(tmp)-1):
            if int(tmp[j+1]) - int(tmp[j]) != sub:
                flag = False
                break
        if flag:
            lst_sum += 1

print(lst_sum)
        