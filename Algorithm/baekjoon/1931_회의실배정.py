# N = int(input())
# timetable = [list(map(int,input().split())) for _ in range(N)]
# max_ = 0
# for _ in range(len(timetable)):
#     li = [timetable[_]]
#     for __ in range(_+1,len(timetable)):
#         if li[-1][1] <= timetable[__][0]:
#             li.append(timetable[__])
#     if max_ < len(li):
#         max_ = len(li)
# print(max_)
# 시간 초과

N = int(input())
timetable = [list(map(int,input().split())) for _ in range(N)]
timetable = sorted(timetable, key=lambda time:(time[1],time[0])) # == timetable.sort()
max_ = 0
lis = [timetable[0]]
for _ in range(1, len(timetable)):
    if lis[-1][1] <= timetable[_][0]:
        lis.append(timetable[_])
print(len(lis))