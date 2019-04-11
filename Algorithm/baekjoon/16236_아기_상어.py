import collections
N = int(input())
t = 0 # 결과값
dxdy = [(-1,0),(1,0),(0,1),(0,-1)] # 상하좌우
size = [0,0] # 처음 상어 사이즈

# 처음 상어 위치를 알아내기
mat = []
for _ in range(N):
    temp = list(map(int,input().split()))
    for __ in range(N):
        if temp[__] == 9:
            i_, j_ = _, __
    mat.append(temp)

# 굳이 처음 상어 위치를 표시할 필요 없으니 0으로 바꾸기
mat[i_][j_] = 0

def BFS(i, j, lis):
    dq = collections.deque()
    dq.append([i,j,0]) # 초기 위치, 이동 거리
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 0xffffffff
    min_ = 0xfffffffffffff
    while dq:
        y,x,cnt=dq.popleft()
        if min_<cnt:
            continue
        for _ in dxdy:
            if 0<=y+_[0]<N and 0<=x+_[1]<N and mat[y+_[0]][x+_[1]] <= len(size) and visited[y+_[0]][x+_[1]] == 0:
                if mat[y+_[0]][x+_[1]] != 0 and mat[y+_[0]][x+_[1]] < len(size) :
                    lis.append([y+_[0],x+_[1],cnt+1])
                    min_ = cnt+1
                visited[y+_[0]][x+_[1]] = 0xffffff
                dq.append([y+_[0],x+_[1],cnt+1])
    return lis

def feeding():
    for _ in range(len(size)):
        if size[_] == 0:
            size[_] = 1
            break
    if 0 not in size:
        for _ in range(len(size)):
            size[_] = 0
        size.append(0)

# 상어 위치에서 BFS를 돌릴거라서 함수를 제작
while True:
    min_lis = sorted(BFS(i_, j_, []), key= lambda x:(x[2],x[0],x[1])) # 제일 위 / 제일 왼쪽
    if min_lis:
        i_, j_, cnt = min_lis[0]
        mat[i_][j_] = 0
        feeding()
        t += cnt
    else:
        break
print(t)