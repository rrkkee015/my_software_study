import collections, copy

N = int(input())
mat = []
dxdy = [(1,0),(0,1),(-1,0),(0,-1)]
size = [0,0]
t = 0
# 상어 처음 위치 찾기
for _ in range(N):
    temp = list(map(int,input().split()))
    for __ in range(len(temp)):
        if temp[__] == 9:
            i_i, i_j = _, __
            temp[__] = 0
    mat.append(temp)

def find(i, j, min_):
    eat = collections.deque()
    eat.append([i,j,0])
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 0xfffff
    minimum = 0xfffffff
    while eat:
        y,x,cnt = eat.popleft()
        if minimum < cnt:
            break
        for _ in dxdy:
            if 0 <= y + _[0] < N and 0 <= x + _[1] < N and mat[y + _[0]][x + _[1]] <= len(size) and visited[y+_[0]][x+_[1]] == 0:
                if mat[y+_[0]][x+_[1]] != 0 and mat[y + _[0]][x + _[1]] < len(size):
                    min_.append([cnt+1, y+_[0], x+_[1]])
                    minimum = cnt + 1
                visited[y + _[0]][x + _[1]] = 0xfffff
                eat.append([y + _[0], x + _[1], cnt + 1])
    return min_

def feeding():
    for _ in range(len(size)):
        if size[_] == 0:
            size[_] = 1
            break
    if 0 not in size:
        for _ in range(len(size)):
            size[_] = 0
        size.append(0)

while True:
    lis = sorted(find(i_i,i_j,[]), key=lambda x : (x[0],x[1],x[2]))
    if lis:
        cnt, i_i, i_j = lis[0]
        t += cnt
        feeding()
        mat[i_i][i_j] = 0
    else:
        break
print(size)
print(t)