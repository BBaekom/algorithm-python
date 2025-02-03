import sys

input = sys.stdin.readline

N = int(input().rstrip())

lst = sorted([tuple(map(int, input().split())) for _ in range(N)])

# 가장 높은 기둥 넓이 + 양 옆 넓이

maxH = lst[0][1]
midx = 0

for i in range(len(lst)):
    if maxH < lst[i][1]:
        maxH = lst[i][1]
        midx = i

# 가정 높은 기둥 넓이
area = maxH

# 왼쪽 넓이 구하기
llen = lst[0][0]
lheight = lst[0][1]

for i in range(1, midx+1):
    if i == midx:
        tmpL = lst[i][0] - llen
        area += (tmpL * lheight)
        break
    if lheight < lst[i][1] and i != midx:
        tmpL = lst[i][0] - llen
        area += (tmpL * lheight)
        lheight = lst[i][1]
        llen = lst[i][0]

# 오른쪽 넓이 구하기
rlen = lst[len(lst)-1][0]
rheight = lst[len(lst)-1][1] 

for i in range(len(lst)-2, midx-1, -1):
    if i == midx:
        tmpR = rlen - lst[i][0]
        area += (tmpR * rheight)
        break
    if rheight < lst[i][1] and i != midx:
        tmpR = rlen - lst[i][0]
        area += (tmpR * rheight)
        rheight = lst[i][1]
        rlen = lst[i][0]

print(area)