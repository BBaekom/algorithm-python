import sys

input = sys.stdin.readline

N = int(input().rstrip())

lst = list(map(int, input().split()))

T, P = map(int, input().split())

tshirts = 0

for h in lst:
    if h == 0:
        continue
    if h % T == 0:
        tshirts += h // T
    else:
        tshirts += h // T + 1

pen = N // P
onePen = N % P 

print(tshirts)
print(pen, onePen)