import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dogam = dict()

for i in range(1, N+1):
    pokemon = input().rstrip()
    dogam[pokemon] = i
    dogam[i] = pokemon

for i in range(M):
    tmp = input().rstrip()
    if tmp.isdigit():
        print(dogam[int(tmp)])
    else:
        print(dogam[tmp])

# O(NlogN) 이하로 풀어야 하는 문제였는데, 시간초과 코드는 O(MN)이었는데 
# 이건, O(N^2)이랑 사실상 같은 시간복잡도였음