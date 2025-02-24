
import sys
input = sys.stdin.readline

name = list(c for c in input().rstrip())

res = ''

alp = dict()
for i in name:
    if i in alp:
        alp[i] += 1
    else:
        alp[i] = 1
alp = sorted(alp.items())
# print(alp)

namuji = []

for i in alp:
    it = i[1] // 2
    if i[1] % 2 == 1:
        namuji.append(i[0])
    for j in range(it):
        res += i[0]
    # print(res)
    # print(namuji)

if len(namuji) > 1:
    print("I'm Sorry Hansoo")
else:
    if not namuji:
        for c in reversed(res):
            res += c
    else:
        for c in reversed(res):
            namuji[0] += c
        res += namuji[0]
        
    print(res)
