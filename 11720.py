import sys

N = int(sys.stdin.readline())
strInt = str(sys.stdin.readline())

sum = 0

for i in range(N):
    sum += int(strInt[i])

print(sum)
