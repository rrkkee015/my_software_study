from itertools import combinations
from copy import deepcopy
N, M, D = map(int,input().split())
list_M = [_ for _ in range(M)]
gameboard = []
temp_turns = -1
for _ in range(N):
    temp = list(map(int,input().split()))
    if 1 in temp and temp_turns == -1:
        temp_turns = _
    gameboard.append(temp)

turns = N - temp_turns + 1
po_arc = list(combinations(list_M, 3))
land = [0] * M
max_ = 0

for position in po_arc:
    ars = [(N, position[0]), (N, position[1]), (N, position[2])]
    top = temp_turns
    kill = 0
    mat = deepcopy(gameboard)
    for turn in range(turns):
        aim = [[], [], []]
        for search in range(top, N):
            for j in range(M):
                if mat[search][j] == 1:
                    for ar in range(len(ars)):
                        if abs(search - ars[ar][0]) + abs(j - ars[ar][1]) <= D:
                            aim[ar].append([search, j, abs(search - ars[ar][0]) + abs(j - ars[ar][1])])

        for shoot in aim:
            shoot = sorted(shoot, key = lambda x : (x[2], x[1]))
            if shoot == []:
                continue
            elif mat[shoot[0][0]][shoot[0][1]] == 1:
                mat[shoot[0][0]][shoot[0][1]] = 0
                kill += 1
        mat.pop()
        mat.insert(0, land)
    if max_ < kill:
        max_ = kill
print(max_)




















# import itertools, copy
#
# N, M, D = map(int,input().split())
# mat = [list(map(int,input().split())) for _ in range(N)]
# sub_mat = [0 for _ in range(M)]
# max_ = 0
#
# # 턴 수 알아내기
# tf = False
# for i in range(N):
#     for j in range(M):
#         if mat[i][j] == 1:
#             temp_t = i
#             tf = True
#     if tf:
#         break
# t = N - temp_t
#
# # 가능한 궁수 배치도
# temp_lis = [_ for _ in range(M)]
# lis = itertools.combinations(temp_lis, 3)
#
# for _ in lis: # 궁수 배치하고
#     play_mat = copy.deepcopy(mat)
#     arrow = [(N, _[0]), (N, _[1]), (N, _[2])]  # 궁수 배치
#     temp = 0
#     incoming = -1
#     for __ in range(t): # 턴 수 만큼 게임 시작
#         dis = [D+1, D+1, D+1]
#         shoot = [0, 0, 0]
#         for i in range(N-1, incoming, -1):
#             for j in range(M):
#                 if play_mat[i][j] == 1:
#                     for ar in range(len(arrow)):
#                         if abs(arrow[ar][0] - i) + abs(arrow[ar][1] - j) < dis[ar]:
#                             dis[ar] = abs(arrow[ar][0] - i) + abs(arrow[ar][1] - j)
#                             shoot[ar] = (i, j)
#                         if abs(arrow[ar][0] - i) + abs(arrow[ar][1] - j) == dis[ar]:
#                             if shoot[ar] and shoot[ar][1] > j:
#                                 shoot[ar] = (i, j)
#         for sh in shoot:
#             if sh:
#                 if play_mat[sh[0]][sh[1]] == 1:
#                     play_mat[sh[0]][sh[1]] = 0
#                     temp += 1
#         play_mat.pop()
#         play_mat.insert(0, sub_mat)
#         incoming += 1
#     if temp > max_:
#         max_ = temp
#
# print(max_)