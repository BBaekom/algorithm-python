import sys
input = sys.stdin.readline

editstr = list(c for c in input().rstrip())
stack = []
N = len(editstr)
M = int(input())

for _ in range(M):
    command = input().split()
    if len(command) == 2:
        # P 문자 인 경우
        editstr.append(command[1])
    else:
        # 나머지인 경우
        if command[0] == 'L':
            if editstr:
                stack.append(editstr.pop(-1))
        elif command[0] == 'D':
            if stack:
                editstr.append(stack.pop(-1))
        else:
            if editstr:
                editstr.pop()
if stack:
    editstr.extend(reversed(stack))
for i in range(len(editstr)):
    print(editstr[i], end='')