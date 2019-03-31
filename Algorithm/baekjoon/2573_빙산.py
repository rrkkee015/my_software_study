import collections

N, M = list(map(int,input().split()))
mat = [list(map(int,input().split())) for _ in range(N)]
setting = [[0] * M for _ in range(N)]
dq = collections.deque()
dxdy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
switch = True
real_result = 0
while switch:
    visited = [[-1] * M for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] != 0 and visited[i][j] == -1:
                result += 1
                dq.append([i,j])
                while dq:
                    y, x = dq.pop()
                    cnt = 0
                    for _ in dxdy:
                        if 0 <= y + _[0] < N and 0 <= x + _[1] < M and mat[y + _[0]][x +_[1]] == 0:
                            cnt += 1
                        if 0 <= y + _[0] < N and 0 <= x + _[1] < M and mat[y + _[0]][x + _[1]] != 0 and visited[y + _[0]][x + _[1]] == -1:
                            dq.append([y + _[0], x + _[1]])
                    visited[y][x] = cnt
    for i in range(N):
        for j in range(M):
            if visited[i][j] != -1:
                mat[i][j] = mat[i][j] - visited[i][j]
                if mat[i][j] < 0:
                    mat[i][j] = 0
    real_result += 1
    if result >= 2:
        break
    if setting == mat:
        real_result = 1
        break
print(real_result - 1)