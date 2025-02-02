import sys

MAX = 10001

input = sys.stdin.readline
n = int(input())
num_list = [0] * MAX

for _ in range(n):
    num_list[int(input())] += 1

for i in range(MAX):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)