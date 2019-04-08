import sys
sys.stdin = open('sample_input.txt','r')

# 동서남북 방향 정하기
ewsn = [(0,0,0), (1,0,1), (2,0,-1), (3,1,0), (4,-1,0)]
block = [(0,0,0,0,0),
         (0,2,4,1,3), # 1번 블록
         (0,2,3,4,1), # 2번 블록
         (0,3,1,4,2), # 3번 블록
         (0,4,1,2,3), # 4번 블록
         (0,2,1,4,3)] # 5번 블록
wall = [0,2,1,4,3]

testcases = int(input())
for tc in range(testcases):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    max_ = 0 # 최댓값
    wh = [[] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if 6 <= mat[i][j] <= 10:
                wh[mat[i][j]].append([i,j])

    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0: # 0일 때 게임 시작
                ini_i = i # 처음 위치
                ini_j = j
                for _ in range(1, len(ewsn)):
                    y = i  # 핀볼 이동 좌표
                    x = j
                    dn = ewsn[_][0]
                    dy = ewsn[_][1]
                    dx = ewsn[_][2]
                    cnt = 0  # 점수
                    while True:
                        y += dy  # 전진
                        x += dx
                        if 0 <= y < N and 0 <= x < N: # 벽 안이면
                            if (y == ini_i and x == ini_j) or mat[y][x] == -1: # 처음 위치이면 혹은 블랙홀이면
                                break # 게임오버
                            elif  1 <= mat[y][x] <= 5: # 블록을 만나면 dy dx를 바꾼다. 점수도 올리고
                                cnt += 1
                                temp = ewsn[block[mat[y][x]][dn]]
                                dn = temp[0]
                                dy = temp[1]
                                dx = temp[2]
                            elif 6 <= mat[y][x] <= 10: # 웜홀이면 다른 웜홀로 좌표를 옮긴다.
                                for _ in wh[mat[y][x]]:
                                    if [y, x] != _:
                                        temp_y = _[0]
                                        temp_x = _[1]
                                y = temp_y
                                x = temp_x
                        if not 0 <= y < N or not 0 <= x < N: # 벽을 벗어나면
                            cnt += 1
                            dn = wall[dn]
                            dy = ewsn[dn][1]
                            dx = ewsn[dn][2]
                    if max_ < cnt:
                        max_ = cnt
    print('#{} {}'.format(tc + 1, max_))