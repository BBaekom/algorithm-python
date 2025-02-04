import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lst = [int(input().rstrip()) for _ in range(K)]

m = max(lst) # 기준이 되는 수
first = 1
end = m
while first <= end:
    mid = (first+end)//2 
    sum = 0
    for i in lst:
        sum += (i // mid)
    if sum < N:
        end = mid - 1
    else:
        first = mid + 1

print(end)