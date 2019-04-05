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
    t = 1
    cnt = 0
    dq.append([sungjin_y, sungjin_x, sungjin_y, sungjin_x, t])
    # 방문한 곳은 1로 채울게요
    visited[sungjin_y][sungjin_x] = 1
    while dq:
        y, x, by, bx, t = dq.popleft() # 현재 위치, 이 전 위치, 현재 시간
        if t <= time:
            cnt += 1
        if t > time:
            continue
        t += 1
        if mat[y][x] == 1: # 현재 위치가 십자가 일 때
            if 0 <= y - 1 and mat[y - 1][x] != 0 and visited[y - 1][x] == 0: # 위에 파이프가 있을 때
                if mat[y - 1][x] == 1 or mat[y - 1][x] == 2 or mat[y - 1][x] == 5 or mat[y - 1][x] == 6:
                    visited[y - 1][x] = 1
                    dq.append([y - 1, x, y, x, t])
            if y + 1 < N and mat[y + 1][x] != 0 and visited[y + 1][x] == 0: # 아래에 파이프가 있을 때
                if mat[y + 1][x] == 1 or mat[y + 1][x] == 2 or mat[y + 1][x] == 4 or mat[y + 1][x] == 7:
                    visited[y + 1][x] = 1
                    dq.append([y + 1, x, y, x, t])
            if 0 <= x - 1 and mat[y][x - 1] != 0 and visited[y][x - 1] == 0: # 왼쪽에 파이프가 있을 때
                if mat[y][x - 1] == 1 or mat[y][x - 1] == 3 or mat[y][x - 1] == 4 or mat[y][x - 1] == 5:
                    visited[y][x - 1] = 1
                    dq.append([y, x - 1, y, x, t])
            if x + 1 < M and mat[y][x + 1] != 0 and visited[y][x + 1] == 0: # 오른쪽에 파이프가 있을 때
                if mat[y][x + 1] == 1 or mat[y][x + 1] == 3 or mat[y][x + 1] == 6 or mat[y][x + 1] == 7:
                    visited[y][x + 1] = 1
                    dq.append([y, x + 1, y, x, t])
        if mat[y][x] == 2: # 현재 위치가 I 일 때
            if 0 <= y - 1 and mat[y - 1][x] != 0 and visited[y - 1][x] == 0:  # 위에 파이프가 있을 때
                if mat[y - 1][x] == 1 or mat[y - 1][x] == 2 or mat[y - 1][x] == 5 or mat[y - 1][x] == 6:
                    visited[y - 1][x] = 1
                    dq.append([y - 1, x, y, x, t])
            if y + 1 < N and mat[y + 1][x] != 0 and visited[y + 1][x] == 0:  # 아래에 파이프가 있을 때
                if mat[y + 1][x] == 1 or mat[y + 1][x] == 2 or mat[y + 1][x] == 4 or mat[y + 1][x] == 7:
                    visited[y + 1][x] = 1
                    dq.append([y + 1, x, y, x, t])
        if mat[y][x] == 3: # 현재 위치가 ㅡ 일 때
            if 0 <= x - 1 and mat[y][x - 1] != 0 and visited[y][x - 1] == 0:  # 왼쪽에 파이프가 있을 때
                if mat[y][x - 1] == 1 or mat[y][x - 1] == 3 or mat[y][x - 1] == 4 or mat[y][x - 1] == 5:
                    visited[y][x - 1] = 1
                    dq.append([y, x - 1, y, x, t])
            if x + 1 < M and mat[y][x + 1] != 0 and visited[y][x + 1] == 0:  # 오른쪽에 파이프가 있을 때
                if mat[y][x + 1] == 1 or mat[y][x + 1] == 3 or mat[y][x + 1] == 6 or mat[y][x + 1] == 7:
                    visited[y][x + 1] = 1
                    dq.append([y, x + 1, y, x, t])
        if mat[y][x] == 4: # 현재 위치가 ㄴ 일 때
            if y - by + x - bx == 0: # 맨홀 들어가자마자 현재 위치임
                if x + 1 < M and mat[y][x + 1] != 0 and visited[y][x + 1] == 0: # 오른쪽에 파이프가 있을 때
                    if mat[y][x + 1] == 1 or mat[y][x + 1] == 3 or mat[y][x + 1] == 6 or mat[y][x + 1] == 7:
                        visited[y][x + 1] = 1
                        dq.append([y, x + 1, y, x, t])
                if 0 <= y - 1 and mat[y - 1][x] != 0 and visited[y - 1][x] == 0:  # 위에 파이프가 있을 때
                    if mat[y - 1][x] == 1 or mat[y - 1][x] == 2 or mat[y - 1][x] == 5 or mat[y - 1][x] == 6:
                        visited[y - 1][x] = 1
                        dq.append([y - 1, x, y, x, t])
            if y - by + x - bx > 0 : # 이 전 값과 현재 값의 차이가 양수이면 위에서 밑으로 들어왔으니 오른쪽으로 가야한다.
                if x + 1 < M and mat[y][x + 1] != 0 and visited[y][x + 1] == 0: # 오른쪽에 파이프가 있을 때
                    if mat[y][x + 1] == 1 or mat[y][x + 1] == 3 or mat[y][x + 1] ==6 or mat[y][x + 1] == 7:
                        visited[y][x + 1] = 1
                        dq.append([y, x + 1, y, x, t])
            if y - by + x - bx < 0: # 이 전 값과 현재 값의 차이가 음수이면 오른쪽에서 왼쪽으로 들어왔으니 위로 가야한다.
                if 0 <= y - 1 and mat[y - 1][x] != 0 and visited[y - 1][x] == 0:  # 위에 파이프가 있을 때
                    if mat[y - 1][x] == 1 or mat[y - 1][x] == 2 or mat[y - 1][x] == 5 or mat[y - 1][x] == 6:
                        visited[y - 1][x] = 1
                        dq.append([y - 1, x, y, x, t])
        if mat[y][x] == 5: # 현재 위치가 ㄱ 뒤집은 모양일 때
            if y - by + x - bx == 0: # 맨홀 들어가자마자 현재 위치임
                if x + 1 < M and mat[y][x + 1] != 0 and visited[y][x + 1] == 0:  # 오른쪽에 파이프가 있을 때
                    if mat[y][x + 1] == 1 or mat[y][x + 1] == 3 or mat[y][x + 1] == 6 or mat[y][x + 1] == 7:
                        visited[y][x + 1] = 1
                        dq.append([y, x + 1, y, x, t])
                if y + 1 <= N and mat[y + 1][x] != 0 and visited[y + 1][x] == 0:  # 아래에 파이프가 있을 때
                    if mat[y + 1][x] == 1 or mat[y + 1][x] == 2 or mat[y + 1][x] == 4 or mat[y + 1][x] == 7:
                        visited[y + 1][x] = 1
                        dq.append([y + 1, x, y, x, t])
            if y - by < 1: # 아래에서 위로 들어온거임 따라서 오른쪽에 있는지 확인해야한다.
                if x + 1 < M and mat[y][x + 1] != 0 and visited[y][x + 1] == 0:  # 오른쪽에 파이프가 있을 때
                    if mat[y][x + 1] == 1 or mat[y][x + 1] == 3 or mat[y][x + 1] == 6 or mat[y][x + 1] == 7:
                        visited[y][x + 1] = 1
                        dq.append([y, x + 1, y, x, t])
            if x - bx < 1: # 오른쪽에서 왼쪽으로 들어온거임 따라서 아래에 있는지 확인해야한다.
                if y + 1 < N and mat[y + 1][x] != 0 and visited[y + 1][x] == 0:  # 아래에 파이프가 있을 때
                    if mat[y + 1][x] == 1 or mat[y + 1][x] == 2 or mat[y + 1][x] == 4 or mat[y + 1][x] == 7:
                        visited[y + 1][x] = 1
                        dq.append([y + 1, x, y, x, t])
        if mat[y][x] == 6:
            if y - by + x - bx == 0:  # 맨홀 들어가자마자 현재 위치임
                if 0 <= x -1 and mat[y][x - 1] != 0 and visited[y][x - 1] == 0: # 왼쪽에 파이프가 있을 때
                    if mat[y][x - 1] == 1 or mat[y][x - 1] == 3 or mat[y][x - 1] == 4 or mat[y][x - 1] == 5:
                        visited[y][x - 1] = 1
                        dq.append([y, x - 1, y, x, t])
                if y + 1 < N and mat[y + 1][x] != 0 and visited[y + 1][x] == 0:  # 아래에 파이프가 있을 때
                    if mat[y + 1][x] == 1 or mat[y + 1][x] == 2 or mat[y + 1][x] == 4 or mat[y + 1][x] == 7:
                        visited[y + 1][x] = 1
                        dq.append([y + 1, x, y, x, t])
            if y - by + x - bx < 0: # 아래에서 위로 들어왔음 왼쪽이 있는지 확인해야함
                if 0 <= x - 1 and mat[y][x - 1] != 0 and visited[y][x - 1] == 0:  # 왼쪽에 파이프가 있을 때
                    if mat[y][x - 1] == 1 or mat[y][x - 1] == 3 or mat[y][x - 1] == 4 or mat[y][x - 1] == 5:
                        visited[y][x - 1] = 1
                        dq.append([y, x - 1, y, x, t])
            if y - by + x - bx > 0: # 왼쪽에서 오른쪽으로 들어왔음 아래에 있는지 확인해야함
                if y + 1 < N and mat[y + 1][x] != 0 and visited[y + 1][x] == 0:  # 아래에 파이프가 있을 때
                    if mat[y + 1][x] == 1 or mat[y + 1][x] == 2 or mat[y + 1][x] == 4 or mat[y + 1][x] == 7:
                        visited[y + 1][x] = 1
                        dq.append([y + 1, x, y, x, t])
        if mat[y][x] == 7:
            if y - by + x - bx ==0: # 맨홀 들어가자마자 현재 위치라면
                if 0 <= y - 1 and mat[y - 1][x] != 0 and visited[y - 1][x] == 0:  # 위에 파이프가 있을 때
                    if mat[y - 1][x] == 1 or mat[y - 1][x] == 2 or mat[y - 1][x] == 5 or mat[y - 1][x] == 6:
                        visited[y - 1][x] = 1
                        dq.append([y - 1, x, y, x, t])
                if 0 <= x -1 and mat[y][x - 1] != 0 and visited[y][x - 1] == 0: # 왼쪽에 파이프가 있을 때
                    if mat[y][x - 1] == 1 or mat[y][x - 1] == 3 or mat[y][x - 1] == 4 or mat[y][x - 1] == 5:
                        visited[y][x - 1] = 1
                        dq.append([y, x - 1, y, x, t])
            if y - by > 0: # 위에서 아래로 들어왔으니까 왼쪽을 확인합니다.
                if 0 <= x - 1 and mat[y][x - 1] != 0 and visited[y][x - 1] == 0: # 왼쪽에 파이프가 있을 때
                    if mat[y][x - 1] == 1 or mat[y][x - 1] == 3 or mat[y][x - 1] == 4 or mat[y][x - 1] == 5:
                        visited[y][x - 1] = 1
                        dq.append([y, x - 1, y, x, t])
            if x - bx > 0: # 왼쪽에서 오른쪽으로 들어왔으니까 위를 확인합니다.
                if 0 <= y - 1 and mat[y - 1][x] != 0 and visited[y - 1][x] == 0:  # 위에 파이프가 있을 때
                    if mat[y - 1][x] == 1 or mat[y - 1][x] == 2 or mat[y - 1][x] == 5 or mat[y - 1][x] == 6:
                        visited[y - 1][x] = 1
                        dq.append([y - 1, x, y, x, t])
    print('#{} {}'.format(tc + 1, cnt))