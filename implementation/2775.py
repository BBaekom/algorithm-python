import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apart = [i for i in range(1, n+1)]

    res = 0

    for i in range(k):
        for j in range(1, n):
            apart[j] += apart[j-1]
    print(apart[-1])
            

# 1층 3호 -> 0층의 1호~3호 = 1 + 2 + 3 = 6
# 2층 3호 -> 1층의 1호~3호 = 1 + 2 + 6 = 9
# 0층 -> 1 2 3 4 ...
# 1층 -> 1 3 6 10 ...
# 2층 -> 1 4 10 15 ...