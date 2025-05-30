import sys

input = sys.stdin.readline

one = int(input().rstrip())
two = int(input().rstrip())

three = one * (two % 10)
four = one * (two // 10 % 10)
five = one * (two // 100 % 10)

print(three)
print(four)
print(five)

res = five * 100 + four * 10 + three

print(res)