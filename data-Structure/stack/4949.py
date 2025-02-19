import sys
input = sys.stdin.readline

while True:
    unbalance = False
    stack = []
    lst = list(c for c in input().rstrip())
    if lst[0] == '.':
        break
    for i in lst:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                unbalance = True
                break
            else:
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                unbalance = True
                break
            else:
                stack.pop()
    if unbalance or stack:
        print('no')
    else:
        print('yes')
                
