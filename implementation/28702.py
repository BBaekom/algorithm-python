import sys
input = sys.stdin.readline

lst = [input().rstrip() for _ in range(3)]

num = 0
for i in range(3):
    if lst[i].isdigit():
        num = int(lst[i]) + (3-i)

if num % 15 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
        