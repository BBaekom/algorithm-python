import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))

N = lst.pop(0)

while len(lst) < N:
    tmp = list(map(int,input().split()))
    for i in tmp:
        lst.append(i)


for i in range(len(lst)):
    tmp = str(lst[i])
    while tmp[-1] == '0':
        tmp = str(int(tmp)//10)
    lst[i] = int(tmp)
    word = ''
    for j in range(len(tmp)-1, -1, -1):
        word += tmp[j]
    lst[i] = int(word)

for i in sorted(lst):
    print(i)