import sys
sys.stdin = open('sample_input.txt','r')

def block(i, j, block_num):
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

testcases = int(input())
for tc in range(testcases):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    hole = [[] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 6:
                hole[board[i][j]].append([i, j])
    max_ = 0
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for _ in dxdy:
                    ini_i = i
                    ini_j = j
                    y = i
                    x = j
                    ty = _[0]
                    tx = _[1]
                    sum_ = 0
                    while True:
                        y += ty
                        x += tx
                        if (y < 0 or N <= y) or (x < 0 or N <= x):
                            ty = -ty
                            tx = -tx
                            sum_ += 1
                        elif (board[y][x] == -1 or (y, x) == (ini_i, ini_j)):
                            if max_ < sum_:
                                max_ = sum_
                            break
                        elif 0 <= y < N and 0 <= x < N:
                            if board[y][x] == 0:
                                continue
                            elif 6 <= board[y][x] <= 10:
                                temp_hole = hole[board[y][x]]
                                for _ in temp_hole:
                                    if [y, x] != _:
                                        temp_y = _[0]
                                        temp_x = _[1]
                                else: # for 문을 끝내고 웜홀을 이동해야한다. 안 그러면 중간에 값이 바뀌어서 이상하게 된다.
                                    y = temp_y
                                    x = temp_x
                            else:
                                ty, tx = block(ty, tx, board[y][x])
                                sum_ += 1
    print('#{} {}'.format(tc + 1, max_))