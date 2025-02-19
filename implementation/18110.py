import sys
input = sys.stdin.readline

n = int(input())

def custom_round(n):
    return int(n + 0.5)

_except = custom_round(n * 0.15)

lst = sorted(list(int(input()) for _ in range(n)))

if lst:
    res = custom_round(sum(lst[_except:n-_except]) / (n - (_except*2)))
else:
    res = 0

print(res)
    