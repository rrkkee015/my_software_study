def dfs(i, j, to):
    global min_
    if (i,j) == (N-1, N-1):
        if min_ > to:
            min_ = to
    elif min_ < to: # 백트래킹
        return
    else:
        for _ in dxdy:
            if 0 <= i + _[0] < N and 0 <= j + _[1] < N:
                dfs(i + _[0], j + _[1], to + mat[i+_[0]][j+_[1]])

testcases = int(input())
for tc in range(testcases):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    result = []
    min_ = 0xfffff
    dxdy = [(0,1),(1,0)]
    dfs(0, 0, mat[0][0])
    print(f'#{tc+1} {min_}')