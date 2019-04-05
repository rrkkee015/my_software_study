import sys
sys.stdin = open('input.txt','r')

import collections

testcases = int(input())
for tc in range(testcases):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    # 전체 최댓값과 위치를 알기 위한 변수를 만듭니다.
    global_max = 0
    po = 0xfffffff
    # 방문했는지 안했는지 확인을 해야하고 몇 개를 이동할 수 있는지 담을 visited를 만듭시다.
    visited = [[0]*N for _ in range(N)]
    # 순회를 위한 dxdy를 만들어 봅시다.
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # BFS를 사용할거니까 BFS를 만들어 봅시다.
    dq = collections.deque()
    # 자 그러면 visited를 순회하면서 0 이면 바로 dq에 넣고 BFS를 실행합니다.
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                dq.append([i, j, 0])
                max_ = 0
                while dq:
                    y, x, cnt = dq.popleft()
                    for _ in dxdy:
                        if 0 <= y + _[0] < N and 0 <= x +_[1] < N and mat[y + _[0]][x + _[1]] - mat[y][x] == 1:
                            visited[y + _[0]][x + _[1]] = 1
                            dq.append([y + _[0], x + _[1], cnt + 1])
                    if max_ < cnt:
                        max_ = cnt
                    if global_max < cnt:
                        global_max = cnt
                # 그 위치에 최댓값을 넣습니다.
                visited[i][j] = max_
    max_ = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == global_max and po > mat[i][j]:
                po = mat[i][j]
    print('#{} {} {}'.format(tc + 1, po, global_max + 1))

# 54321이라는 숫자가 있으면 5에서 한번 순회를 마치면 굳이 4 3 2 1을 할 필요는 없습니다.
# 왜냐면 5에서 돈 것이 이미 최댓값이 될 거니까요.
# 그리고 숫자는 겹치지 않고 자기보다 1 큰 숫자는 하나 밖에 없으니