import sys
input = sys.stdin.readline

K, L = map(int, input().split())

st_num = dict()
lst = []

for i in range(L):
    tmp = input().rstrip()
    st_num[tmp] = i

st_num = sorted(st_num.items(), key=lambda x:x[1])

if K > len(st_num):
    N = len(st_num)
else:
    N = K

for i in range(N):
    print(st_num[i][0]) 