import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

x = ((c * e) - (f * b)) // ((a * e) - (d * b)) 
y = ((c * d) - (f * a)) // ((b * d) - (a * e))

print(x, y)