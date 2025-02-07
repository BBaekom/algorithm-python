import sys
input = sys.stdin.readline

n = int(input())

company = dict()

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        company[name] = status
    else:
        dict.pop(company, name)

for i in sorted(company, reverse=True):
    print(i)