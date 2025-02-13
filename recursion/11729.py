import sys
input = sys.stdin.readline

N = int(input())

def func(n, one, two, three):
    if n == 1:
        print(one, three)
        return
    else:
        func(n-1, one, three, two)
        print(one, three)
        func(n-1, two, one, three)

print(2**N - 1)
func(N, 1, 2, 3)