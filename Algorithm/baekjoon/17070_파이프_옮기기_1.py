# from collections import deque
# import sys
# sys.setrecursionlimit(10**9)
#
# def dfs_(s, e):
#     global cnt
#     if e[0] == N-1 and e[1] == N-1:
#         cnt+=1
#         return
#     status = [e[0]-s[0],e[1]-s[1]] # 상태 확인
#     if status == [0,1]: # 가로
#         if e[1]+1<N and mat[e[0]][e[1]+1] != 1:
#             ne = [e[0],e[1]+1]
#             dfs(e, ne)
#         if e[0]+1<N and e[1]+1<N and mat[e[0]+1][e[1]] != 1 and mat[e[0]][e[1]+1] != 1 and mat [e[0]+1][e[1]+1] != 1:
#             ne = [e[0]+1,e[1]+1]
#             dfs(e, ne)
#     elif status == [1,1]: # 대각선
#         if e[1]+1<N and mat[e[0]][e[1]+1] != 1:
#             ne = [e[0],e[1]+1]
#             dfs(e, ne)
#         if e[0]+1<N and e[1]+1<N and mat[e[0]+1][e[1]] != 1 and mat[e[0]][e[1]+1] != 1 and mat [e[0]+1][e[1]+1] != 1:
#             ne = [e[0]+1,e[1]+1]
#             dfs(e, ne)
#         if e[0]+1<N and mat[e[0]+1][e[1]] != 1:
#             ne = [e[0]+1,e[1]]
#             dfs(e, ne)
#     elif status == [1,0]: # 세로
#         if e[0]+1<N and mat[e[0]+1][e[1]] != 1:
#             ne = [e[0]+1,e[1]]
#             dfs(e, ne)
#         if e[0]+1<N and e[1]+1<N and mat[e[0]+1][e[1]] != 1 and mat[e[0]][e[1]+1] != 1 and mat [e[0]+1][e[1]+1] != 1:
#             ne = [e[0]+1,e[1]+1]
#             dfs(e, ne)
# #
# N=int(input())
# mat=[list(map(int,input().split())) for _ in range(N)]
# i_s=[0,0]
# i_e=[0,1]
# cnt=0
# dfs(i_s, i_e)
# print(cnt)
# dfs = deque()
# dfs.append([i_s, i_e])
# while dfs:
#     s,e = dfs.pop()
#     if e[0] == N-1 and e[1] == N-1: # 도착했니?
#         cnt+=1
#         continue
#     status = [e[0]-s[0], e[1]-s[1]]  # 상태 확인
#     if status == [0, 1]:  # 가로
#         if e[1] + 1 < N and mat[e[0]][e[1] + 1] != 1:
#             ne = [e[0], e[1] + 1]
#             dfs.append([e, ne])
#         if e[0] + 1 < N and e[1] + 1 < N and mat[e[0] + 1][e[1]] != 1 and mat[e[0]][e[1] + 1] != 1 and mat[e[0] + 1][
#             e[1] + 1] != 1:
#             ne = [e[0] + 1, e[1] + 1]
#             dfs.append([e, ne])
#     elif status == [1, 1]:  # 대각선
#         if e[1] + 1 < N and mat[e[0]][e[1] + 1] != 1:
#             ne = [e[0], e[1] + 1]
#             dfs.append([e, ne])
#         if e[0] + 1 < N and e[1] + 1 < N and mat[e[0] + 1][e[1]] != 1 and mat[e[0]][e[1] + 1] != 1 and mat[e[0] + 1][
#             e[1] + 1] != 1:
#             ne = [e[0] + 1, e[1] + 1]
#             dfs.append([e, ne])
#         if e[0] + 1 < N and mat[e[0] + 1][e[1]] != 1:
#             ne = [e[0] + 1, e[1]]
#             dfs.append([e, ne])
#     elif status == [1, 0]:  # 세로
#         if e[0] + 1 < N and mat[e[0] + 1][e[1]] != 1:
#             ne = [e[0] + 1, e[1]]
#             dfs.append([e, ne])
#         if e[0] + 1 < N and e[1] + 1 < N and mat[e[0] + 1][e[1]] != 1 and mat[e[0]][e[1] + 1] != 1 and mat[e[0] + 1][
#             e[1] + 1] != 1:
#             ne = [e[0] + 1, e[1] + 1]
#             dfs.append([e, ne])
#
# print(cnt)
import collections

N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
isgood = [(0, 1, 0), (1, 0, 1), (1, 1, -1)]
pipe = collections.deque()
pipe.append([0, 1, 0, 0])
while pipe:
    i_e, j_e, i_s, j_s = pipe.pop()
    status = (i_e - i_s, j_e - j_s)
    if i_e == N - 2 and j_e == N - 2:
        cnt += 1
        continue
    elif i_e == N - 2 and j_e == N - 1 and mat[i_e][j_e] == 0 and status != (0, 1):
        cnt += 1
        continue
    elif i_e == N - 1 and j_e == N - 2 and status != (1, 0) and mat[i_e][j_e] == 0:
        cnt += 1
        continue
    else:
        tf = True
        for _ in isgood:
            if i_e + _[0] < N and j_e + _[1] < N and mat[i_e + _[0]][j_e + _[1]] != 1:
                if _[2] == 0 and status != (1, 0):
                    pipe.append([i_e, j_e + 1, i_e, j_e])
                elif _[2] == 1 and status != (0, 1):
                    pipe.append([i_e + 1, j_e, i_e, j_e])
            else:
                tf = False
        if tf:
            pipe.append([i_e + 1, j_e + 1, i_e, j_e])
print(cnt)

# def pipe(i_e, j_e, i_s, j_s):
#     global cnt
#     if i_e == N - 1 and j_e == N - 1:
#         cnt += 1
#         return
#     else:
#         status = (i_e - i_s, j_e - j_s)
#         tf = True
#         for _ in isgood:
#             if i_e + _[0] < N and j_e + _[1] < N and mat[i_e + _[0]][j_e + _[1]] != 1:
#                 if _[2] == 0 and status != (1, 0):
#                     pipe(i_e, j_e + 1, i_e, j_e)
#                 elif _[2] == 1 and status != (0, 1):
#                     pipe(i_e + 1, j_e, i_e, j_e)
#             else:
#                 tf = False
#         if tf:
#             pipe(i_e + 1, j_e + 1, i_e, j_e)
#
# pipe(0, 1, 0, 0)



























