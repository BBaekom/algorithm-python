import sys

input = sys.stdin.readline

N = int(input().rstrip())
cards = sorted(list(map(int, input().split())))

M = int(input().rstrip())
candidate = list(map(int, input().split()))

count = {}
# 딕셔너리 초기화
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

def binarySearch(cards, candidate):
    res = []
    for i in range(M):
        start = 0
        end = len(cards)-1
        target = candidate[i]
        res.append(0)
        while start <= end:
            mid = (start + end) // 2
            if cards[mid] == target:
                res[-1] = count.get(target)
                break
            elif cards[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
    return res

result = binarySearch(cards, candidate)
print(*result)