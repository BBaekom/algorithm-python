import sys

input = sys.stdin.readline

H, M = map(int, input().split())

if M >= 45:
    print(H, M-45)
else:
    if H == 0:
        print(23, 60-(45-M))
    else:
        print(H-1, 60-(45-M))