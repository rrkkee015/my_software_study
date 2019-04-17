N, M = map(int,input().split())
# 로봇 초기값
i, j, to = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]

check = [(0,-1),(-1,0),(0,1),(1,0)] # 로봇 왼쪽 확인용
go = [(-1,0),(0,1),(1,0),(0,-1)] # 로봇 전진 용
back = [(1,0),(0,-1),(-1,0),(0,1)] # 로봇 후진 용
dxdy = [3, 0, 1, 2] # 로봇 방향 꺾기용
result = 0

while True:
    if mat[i][j] == 0:  # 현재 위치가 청소 안 되어 있다면 청소하고
        mat[i][j] = 2
        result += 1
    for _ in go:
        if not (0<=i+_[0]<N and 0<=j+_[1]<M):
            continue
        elif mat[i+_[0]][j+_[1]] == 0: # 청소할 곳이 하나라도 있으면
            break
    else: # 하나라도 없으면 후진 해야한다.
        if mat[i+back[to][0]][j+back[to][1]] == 1: # 뒤가 벽이면 작동 중지
            break
        else: # 뒤가 빈 공간이면 후진
            i += back[to][0]
            j += back[to][1]
            continue
    check_i, check_j = check[to][0], check[to][1]
    if mat[i + check_i][j + check_j] == 0: # 왼쪽이 청소 안되어 있으면
        to = dxdy[to] # 방향 꺾고
        i += go[to][0] # 전진
        j += go[to][1]
    elif mat[i + check_i][j + check_j] >= 1: # 왼쪽이 벽이거나 청소 되어 있으면
        to = dxdy[to] # 방향만 꺾는다.

print(result)