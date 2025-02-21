answers = [1,3,2,4,2]
answer = []
one = [1, 2, 3, 4, 5]
two = [2, 1, 2, 3, 2, 4, 2, 5]
three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
# 1번 수포자 검사
cnt_one = 0
lst = []
cnt = 0
while True:
    if cnt_one > len(answers):
        break
    if cnt == len(one):
        cnt = 0
    if answers[cnt_one] != one[cnt]:
        cnt_one += 1
        lst.append(cnt_one)
        break
    cnt_one += 1
    cnt += 1
cnt_two = 0
cnt = 0
while True:
    if cnt_two > len(answers):
        break
    if cnt == len(two):
        cnt = 0
    if answers[cnt_two] != two[cnt]:
        cnt_two += 1
        lst.append(cnt_two)
        break
    cnt_two += 1
    cnt += 1
cnt_three = 0
cnt = 0
while True:
    if cnt_three > len(answers):
        break
    if cnt == len(three):
        cnt = 0
    if answers[cnt_three] != three[cnt]:
        cnt_three += 1
        lst.append(cnt_three)
        break
    cnt_three += 1
    cnt += 1
m = max(lst)
for i in range(3):
    if m == lst[i]:
        answer.append(i+1)

print(answer)