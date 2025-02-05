import sys

input = sys.stdin.readline

N = int(input().rstrip())
res = 0

for _ in range(N):
    tmp = input().rstrip()
    candidates = []
    cntA = cntB = 0
    for i in range(len(tmp)):
        if tmp[i] == 'A': cntA += 1
        else: cntB += 1
        candidates.append(tmp[i])
    
    st = []
    for i in candidates:
        if not st:
            st.append(i)
        elif st[-1] == i:
            st.pop()
        else:
            st.append(i)

    if not st:
        res += 1
        
print(res)