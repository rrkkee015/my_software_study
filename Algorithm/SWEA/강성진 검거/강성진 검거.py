import sys
sys.stdin = open('sample_input.txt','r')

import collections

testcases = int(input())
for tc in range(testcases):
    N, M, sungjin_y, sungjin_x, time = list(map(int,input().split()))
    mat = [list(map(int,input().split())) for _ in range(N)]

    # 똑같은 곳 못가게 visited도 만듭시다.
    visited = [[0] * M for _ in range(N)]

    dq = collections.deque()
    # 성지니를 처음 위치에 넣읍시다. 이 때는 1시간 뒤입니다.
    ing = 1
    dq.append([sungjin_y, sungjin_x, sungjin_y, sungjin_y, ing])
    # 방문한 곳은 1로 채울게요
    visited[sungjin_y][sungjin_x] = 1
    while t != time:
        y, x, by, bx, t = dq.popleft()
        t += 1
        if mat[y][x] == 1: # 현재 위치가 십자가 일 때
            if y + 1 < N and mat[y + 1][x] != 0: # 위에 파이프가 있을 때
                if mat[y + 1][x] == 1 or mat[y + 1][x] == 2 or mat[y + 1][x] == 5 or mat[y + 1][x] == 6:
                    visited[y + 1][x] = 1
                    dq.append([y + 1, x, y, x, t])
            if 0 <= y - 1 and mat[y - 1][x] != 0: # 아래에 파이프가 있을 때
                if mat[y - 1][x] == 1 or mat[y - 1][x] == 2 or mat[y - 1][x] == 4 or mat[y - 1][x] == 7:
                    visited[y - 1][x] = 1
                    dq.append([y - 1, x, y, x, t])
            if 0 <= x - 1 and mat[y][x - 1] != 0: # 왼쪽에 파이프가 있을 때
                if mat[y][x - 1] == 1 or mat[y][x - 1] == 3 or mat[y][x - 1] == 4 or mat[y][x - 1] == 5:
                    visited[y][x - 1] = 1
                    dq.append([y, x - 1, y, x, t])
            if x + 1 < N and mat[y][x + 1] != 0: # 오른쪽에 파이프가 있을 때
                if mat[y][x + 1] == 1 or mat[y][x + 1] == 3 or mat[y][x + 1] == 6 or mat[y][x + 1] == 7:
                    visited[y][x + 1] = 1
                    dq.append([y, x + 1, y, x, t])
        if mat[y][x] == 2: # 현재 위치가 I 일 때
            if y + 1 < N and mat[y + 1][x] != 0: # 위에 파이프가 있을 때
                if mat[y + 1]