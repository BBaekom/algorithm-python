import sys

input = sys.stdin.readline

arr = []

arr = input().split()

arr2 = arr.copy()

if sorted(arr2) == arr:
    print("ascending")
elif sorted(arr2, reverse=True) == arr:
    print("descending")
else:
    print("mixed")