from collections import deque

while True:
    w, h = map(int,input().split())
    if w == 0 or h == 0:
        break
    mat = [list(map(int,input().split())) for _ in range(h)]

    result = 0
    dxdy = [(1,0),(-1,0),(0,1),(0,-1),(-1,1),(-1,-1),(1,-1),(1,1)]
    q = deque()

    for i in range(h):
        for j in range(w):
            if mat[i][j] == 1:
                q.append([i,j])
                while q:
                    temp_i, temp_j = q.popleft()
                    for _ in dxdy:
                        if 0 <= temp_i + _[0] < h and 0 <= temp_j + _[1] < w and mat[temp_i + _[0]][temp_j + _[1]] == 1:
                            mat[temp_i + _[0]][temp_j + _[1]] = 0
                            q.append([temp_i + _[0], temp_j + _[1]])
                result += 1
    print(result)