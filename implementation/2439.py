import sys

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(' ')

for i in range(n):
    arr.append('*')
    arr.pop(0)
    for j in arr:
        print(j, end='')
    print()
