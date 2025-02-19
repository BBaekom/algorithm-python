import sys
input = sys.stdin.readline

N = int(input())

# N = 5a + 3b
# res = 0

# while N >= 0:
#     if N % 5 == 0:
#         res += (N // 5)
#         print(res)
#         break
#     N -= 3
#     res += 1
# else:
#     print(-1)

# dp 풀이
res = [-1] * 5001 # 5랑 3으로 만들어지지 않는 수는 모두 -1이기 때문에 -1로 초기화
res[3] = res[5] = 1

for i in range(6, N+1):
    if i % 5 == 0:
        res[i] = res[i-5] + 1
    elif i % 3 == 0:
        res[i] = res[i-3] + 1
    # 18 경우 res[15] res[13]
    elif res[i-3] > 0 and res[i-5] > 0:
        res[i] = min(res[i-3], res[i-5]) + 1
    
print(res[N])
