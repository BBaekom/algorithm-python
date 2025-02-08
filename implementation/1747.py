import sys
input = sys.stdin.readline

N = int(input())

def is_pelindrome(i):
    # tmp = str(i)
    # for j in range(len(tmp)//2):
    #     right = len(tmp) - j - 1
    #     if tmp[j] != tmp[right]:
    #         return False
    # return True
    i = str(i)
    return i == i[::-1]

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    if is_prime(N) and is_pelindrome(N):
        print(N)
        break
    else:
        N += 1