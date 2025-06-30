import sys
input = sys.stdin.readline

word = input().rstrip().upper()

lst = list(set(word))

cnt = []

for c in lst:
    n = word.count(c)
    cnt.append(n) 

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(lst[cnt.index(max(cnt))])