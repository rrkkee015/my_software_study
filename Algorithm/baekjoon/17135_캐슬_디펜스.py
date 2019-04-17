import itertools, copy

N, M, D = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
sub_mat = [0 for _ in range(M)]
max_ = 0

# 턴 수 알아내기
tf = False
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            temp_t = i
            tf = True
    if tf:
        break
t = N - temp_t

# 가능한 궁수 배치도
temp_lis = [_ for _ in range(M)]
lis = itertools.combinations(temp_lis, 3)

for _ in lis: # 궁수 배치하고
    play_mat = copy.deepcopy(mat)
    arrow = [(N, _[0]), (N, _[1]), (N, _[2])]  # 궁수 배치
    temp = 0
    incoming = -1
    for __ in range(t): # 턴 수 만큼 게임 시작
        dis = [D+1, D+1, D+1]
        shoot = [0, 0, 0]
        for i in range(N-1, incoming, -1):
            for j in range(M):
                if play_mat[i][j] == 1:
                    for ar in range(len(arrow)):
                        if abs(arrow[ar][0] - i) + abs(arrow[ar][1] - j) < dis[ar]:
                            dis[ar] = abs(arrow[ar][0] - i) + abs(arrow[ar][1] - j)
                            shoot[ar] = (i, j)
                        if abs(arrow[ar][0] - i) + abs(arrow[ar][1] - j) == dis[ar]:
                            if shoot[ar] and shoot[ar][1] > j:
                                shoot[ar] = (i, j)
        for sh in shoot:
            if sh:
                if play_mat[sh[0]][sh[1]] == 1:
                    play_mat[sh[0]][sh[1]] = 0
                    temp += 1
        play_mat.pop()
        play_mat.insert(0, sub_mat)
        incoming += 1
    if temp > max_:
        max_ = temp

print(max_)