import sys

num = 1001

def prime(arr):
    newArr = [i for i in range(num)]
    newArr[0] = newArr[1] = 0
    for i in range(2, int(num**0.5)+1):
        if newArr[i] != 0:
            for j in range(i*i, num, i):
                newArr[j] = 0
    result = []
    for i in range(len(arr)):
        if arr[i] in newArr:
            result.append(arr[i])
    return result

input = sys.stdin.readline

N = int(input().rstrip())

arr = list(map(int, input().split()))

print(len(prime(arr)))