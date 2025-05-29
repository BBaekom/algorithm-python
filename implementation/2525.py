import sys

input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input().rstrip())

hour = A + C // 60
minute = B + C % 60

if minute >= 60:
    hour += 1
    minute -= 60

if hour >= 24:
    hour -= 24

print(hour, minute)