import sys

input = sys.stdin.readline
n = int(input())

zero = 0
fac_Num = 1

for i in range (1, n+1, 1):
    fac_Num *= i

while fac_Num != 0 :
    num = fac_Num % 10
    if num != 0:
        break
    zero += 1
    fac_Num //= 10

print(zero)