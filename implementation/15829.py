import sys
input = sys.stdin.readline

r = 31
M = 1234567891

alp = dict()

for i in range(1, 27):
    alp[chr(i+96)] = i

L = int(input())
lst = [c for c in input().rstrip()]

H = 0
for i in range(L):
    H += alp[lst[i]] * (r**i)
    H %= M

print(H)