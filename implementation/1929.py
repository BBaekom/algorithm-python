import sys

input = sys.stdin.readline

num = 1000001  

def prime(M, N):
    arr = [True] * num 
    arr[0] = arr[1] = False  

    for i in range(2, int(num**0.5) + 1):  
        if arr[i]: 
            for j in range(i * i, num, i): 
                arr[j] = False

    for i in range(M, N + 1):
        if arr[i]:
            print(i)

M, N = map(int, input().split())
prime(M, N)