import sys
sys.stdin = open('sample_input.txt','r')
# 성진이가 말하길 이 문제는 굳이 재귀로 풀 필요가 없는게 갔다가 돌아오면서 값을 꺼내올 필요가 없기 때문이다.
# 블록을 만나면 어떻게 행동을 할 건지 함수를 구현합니다.
def block(i, j, block_num): # 진행방향과 함수의 번호를 입력 받습니다.
    if block_num == 1:
        if (i, j) == (1, 0):
            return (0, 1)
        elif (i, j) == (0, -1):
            return (-1, 0)
        else:
            return (-i, -j)
    if block_num == 2:
        if (i, j) == (-1, 0):
            return (0, 1)
        elif (i, j) == (0, -1):
            return (1, 0)
        else:
            return (-i, -j)
    if block_num == 3:
        if (i, j) == (0, 1):
            return (1, 0)
        elif (i, j) == (-1, 0):
            return (0, -1)
        else:
            return (-i, -j)
    if block_num == 4:
        if (i, j) == (1, 0):
            return (0, -1)
        elif (i, j) == (0, 1):
            return (-1, 0)
        else:
            return (-i, -j)
    if block_num == 5:
        return (-i, -j)

def dfs(y, x, ty, tx, sum_):
    global ini_i, ini_j, max_, start
    y += ty
    x += tx
    if (y < 0 or N <= y) or (x < 0 or N <= x):
        # 벽이면 그 자리에서 점수를 1 더하고 방향에 따라서 방향을 바꾸고 dfs로 넘기도록 합시다.
        dfs(y, x, -ty, -tx, sum_ + 1)
    # 종료 시점은 넘어온 위치가 -1 이거나 시작 위치이면 정지합니다.
    elif (board[y][x] == -1 or (y, x) == (ini_i, ini_j)):
        # 그 때 점수를 비교해 줍시다.
        if max_ < sum_:
            max_ = sum_
        return
    # 그 지점에서 방향으로 출발합시다. 출발 하기 전에 그 지점이 벽인지 아닌지를 확인합니다.
    elif 0 <= y < N and 0 <= x < N:
        # 벽이 아니면 이동을 하는데, 만약 그 지점에 아무것도 없는 0 이라면, 진행 방향으로 이동합니다.
        if board[y][x] == 0:
            dfs(y, x, ty, tx, sum_)
        # 만약 웜홀이면 다른 웜홀로 이동할 수 있도록 합니다. 미리 제작한 웜홀 배열을 사용합니다.
        elif 6 <= board[y][x] <= 10:
            temp_hole = hole[board[y][x]]
            for _ in temp_hole:
                if [y, x] != _: # 만약 현재 위치와 다른 웜홀이면 그 곳으로 보냅니다.
                    dfs(_[0], _[1], ty, tx, sum_)
        # 만약 위에 모든 것이 아니면 블록 함수를 실행합니다.
        else:
            ty, tx = block(ty, tx, board[y][x])
            # 바꾼 방향을 넘기고 점수도 올려줍니다.
            dfs(y, x, ty, tx, sum_ + 1)

testcases = int(input())
for tc in range(testcases):
    # 보드 크기, 게임판을 받습니다.
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    # 웜홀의 위치를 받아 보겠슴니당
    hole = [[] for _ in range(11)] # 이거 * 연산자로 만들면 하나 바꾸면 다 바뀜
    # 게임판을 돌면서 웜홀의 번호에 맞춰서 그 웜홀의 인덱스를 집어 넣습니다.
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 6:
                hole[board[i][j]].append([i, j])
    # 최댓값을 결정할 max_ 인자를 만듭니다.
    max_ = 0
    # 이제 본격적인 dfs 함수를 구현해봅니다. # 게임판을 돌면서 0 인 부븐은 핀볼의 시작 위치입니다.
    # 방향을 정하기 위해서 dxdy를 만듭니다.
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # 시작 위치에서 방향과 함께 함수에 같이 넣어서 보내주도록 합니다.
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for _ in dxdy:
                    # 시작위치, 방향, 점수를 보내도록 합시다. # 단, 시작 위치를 기억해야 나중에 시작위치로 돌아오면 처리가 가능합니다.
                    ini_i = i
                    ini_j = j
                    dfs(i, j, _[0], _[1], 0)
    # 결과값을 출력합니다.
    print('#{} {}'.format(tc + 1, max_))