import sys
sys.stdin = open('input.txt','r')

import itertools, copy
N, M, D = list(map(int,input().split()))
mat = [list(map(int,input().split())) for _ in range(N)]
# 맨 위에 있는 적 찾기
tf = False
gameover = 1
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            turn = i
            tf = True
            break
    if tf:
        break
else:
    gameover = 0
if gameover == 0:
    print(0)
else:
    real_turn = N - turn
    # 궁수를 위치에 배치를 하려면 조합을 써야한다.
    # 궁수 배치 경우의 수
    temp_lis = [_ for _ in range(M)]
    archers = list(itertools.combinations(temp_lis, 3))
    test = 0
    # 최대로 죽일 수 있는 적 수
    max_ = 0
    for test in range(len(archers)):
        attack = copy.deepcopy(mat)
        cnt = 0
        turn = real_turn
        while turn != 0:
            used = [0, 0, 0]
            kill = 0
            tf = False
            for _ in range(N - 1, N - 1 - D, -1):
                for __ in range(M):
                    if attack[_][__] == 1:
                        for archer in range(len(archers[test])):
                            if abs(_ - N) + abs(__ - archers[test][archer]) <= D and used[archer] == 0:
                                used[archer] = 1
                                attack[_][__] = 0
                                kill += 1
                                cnt += 1
                                if kill == 3:
                                    tf = True
                                    break
                                break
                if tf:
                    break
            turn -= 1
            attack.pop()
            attack.insert(0,[0] * M)
        if max_ < cnt:
            max_ = cnt
    print(max_)