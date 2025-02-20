import sys
input = sys.stdin.readline

N = int(input())

timetable = sorted(list(list(map(int, input().split())) for _ in range(N)), key=lambda x: (x[1], x[0]))
# print(timetable)

seminar_cnt = 1

start = timetable[0][0]
end = timetable[0][1]
for i in range(len(timetable)):
    if i == 0:
        continue
    if timetable[i][0] >= end:
        seminar_cnt += 1
        start = timetable[i][0]
        end = timetable[i][1]
        
print(seminar_cnt)