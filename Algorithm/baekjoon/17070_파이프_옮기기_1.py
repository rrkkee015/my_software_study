from collections import deque
import sys
sys.setrecursionlimit(10**9)

def dfs_(s, e):
    global cnt
    if e[0] == N-1 and e[1] == N-1:
        cnt+=1
        return
    status = [e[0]-s[0],e[1]-s[1]] # 상태 확인
    if status == [0,1]: # 가로
        if e[1]+1<N and mat[e[0]][e[1]+1] != 1:
            ne = [e[0],e[1]+1]
            dfs(e, ne)
        if e[0]+1<N and e[1]+1<N and mat[e[0]+1][e[1]] != 1 and mat[e[0]][e[1]+1] != 1 and mat [e[0]+1][e[1]+1] != 1:
            ne = [e[0]+1,e[1]+1]
            dfs(e, ne)
    elif status == [1,1]: # 대각선
        if e[1]+1<N and mat[e[0]][e[1]+1] != 1:
            ne = [e[0],e[1]+1]
            dfs(e, ne)
        if e[0]+1<N and e[1]+1<N and mat[e[0]+1][e[1]] != 1 and mat[e[0]][e[1]+1] != 1 and mat [e[0]+1][e[1]+1] != 1:
            ne = [e[0]+1,e[1]+1]
            dfs(e, ne)
        if e[0]+1<N and mat[e[0]+1][e[1]] != 1:
            ne = [e[0]+1,e[1]]
            dfs(e, ne)
    elif status == [1,0]: # 세로
        if e[0]+1<N and mat[e[0]+1][e[1]] != 1:
            ne = [e[0]+1,e[1]]
            dfs(e, ne)
        if e[0]+1<N and e[1]+1<N and mat[e[0]+1][e[1]] != 1 and mat[e[0]][e[1]+1] != 1 and mat [e[0]+1][e[1]+1] != 1:
            ne = [e[0]+1,e[1]+1]
            dfs(e, ne)
        
N=int(input())
mat=[list(map(int,input().split())) for _ in range(N)]
i_s=[0,0]
i_e=[0,1]
cnt=0
# dfs(i_s, i_e)
dfs = deque()
dfs.append([i_s, i_e])
while dfs:
    s,e = dfs.pop()
    if e[0] == N-1 and e[1] == N-1: # 도착했니?
        cnt+=1
        continue
    status = [e[0]-s[0], e[1]-s[1]]  # 상태 확인
    if status == [0, 1]:  # 가로
        if e[1] + 1 < N and mat[e[0]][e[1] + 1] != 1:
            ne = [e[0], e[1] + 1]
            dfs.append([e, ne])
        if e[0] + 1 < N and e[1] + 1 < N and mat[e[0] + 1][e[1]] != 1 and mat[e[0]][e[1] + 1] != 1 and mat[e[0] + 1][
            e[1] + 1] != 1:
            ne = [e[0] + 1, e[1] + 1]
            dfs.append([e, ne])
    elif status == [1, 1]:  # 대각선
        if e[1] + 1 < N and mat[e[0]][e[1] + 1] != 1:
            ne = [e[0], e[1] + 1]
            dfs.append([e, ne])
        if e[0] + 1 < N and e[1] + 1 < N and mat[e[0] + 1][e[1]] != 1 and mat[e[0]][e[1] + 1] != 1 and mat[e[0] + 1][
            e[1] + 1] != 1:
            ne = [e[0] + 1, e[1] + 1]
            dfs.append([e, ne])
        if e[0] + 1 < N and mat[e[0] + 1][e[1]] != 1:
            ne = [e[0] + 1, e[1]]
            dfs.append([e, ne])
    elif status == [1, 0]:  # 세로
        if e[0] + 1 < N and mat[e[0] + 1][e[1]] != 1:
            ne = [e[0] + 1, e[1]]
            dfs.append([e, ne])
        if e[0] + 1 < N and e[1] + 1 < N and mat[e[0] + 1][e[1]] != 1 and mat[e[0]][e[1] + 1] != 1 and mat[e[0] + 1][
            e[1] + 1] != 1:
            ne = [e[0] + 1, e[1] + 1]
            dfs.append([e, ne])

print(cnt)