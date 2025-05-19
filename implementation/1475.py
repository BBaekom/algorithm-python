import sys

input = sys.stdin.readline

N = input().rstrip()
lst = [0 for _ in range(10)]

for n in N:
    num = int(n)
    if num == 6 or num == 9:
        if lst[6] < lst[9]:
            lst[6] += 1
        elif lst[6] > lst[9]:
            lst[9] += 1
        else:
            lst[num] += 1
            
    else:
        lst[num] += 1
               
        

print(max(lst))