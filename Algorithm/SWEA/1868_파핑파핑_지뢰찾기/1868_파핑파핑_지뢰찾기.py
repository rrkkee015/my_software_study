import sys
sys.stdin = open('input.txt','r')
import collections
testcases = int(input())

for tc in range(testcases):
    N = int(input())
    # 간단한 조작을 위해서 배열로 입력을 받도록 합시다.
    # 이거 벽체크하기 좀 까다로우니까 그냥 아싸리 패딩을 만듭시다.
    mat = [[7 for _ in range(N+2)]]
    # 정답을 위한 cnt
    cnt = 0
    for _ in range(N):
        temp = [7]
        for __ in input():
            temp.append(__)
        temp.append(7)
        mat.append(temp)
    # 8 방향을 돌아봐야하니 8 방향 탐색을 위한 배열을 만듭니다.
    mat.append([7 for _ in range(N+2)])
    dxdy = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    # BFS를 위한 deque을 만듭니다. # DFS를 안쓰는 이유론, 재귀로 짜면 N 이 300*300이라서 터질거 같음
    dq = collections.deque()
    # 이제 순회를 하는데, 돌아다니다가 8 방향에 지뢰가 없으면 걔는 0이니까 걔 중심으로 BFS를 돌립니다.
    # 긴장
    for i in range(1,N+1):
        for j in range(1,N+1):
            # 만약 지뢰가 아닌 땅을 만나면 8 방향 탐색
            if mat[i][j] == '.':
                for _ in dxdy:
                    # 그 후 8방향 탐색
                    if mat[i+_[0]][j+_[1]] == '.':
                        # 지뢰가 없으면 계속 탐색
                        continue
                    elif mat[i+_[0]][j+_[1]] == '*': # 지뢰가 있으면 그냥 지나갑시다.
                        break
                else:
                    # 주변에 전부 지뢰가 없으니 걔는 클릭을 해야겠죠?
                    cnt += 1
                    # for 문이 다 돌았다는 말은 주변에 지뢰가 없다는 말이니
                    # 그 중심으로 BFS를 시작합시다.
                    dq.append([i,j])
                    mat[i][j] = 0
                    while dq:
                        y,x = dq.pop()
                        # 귀찮지만 또 8방향 탐색 주변에 지뢰가 있나 확인합니다.
                        for _ in dxdy:
                            if mat[y+_[0]][x+_[1]] == '*':
                                # 근데 주변에 지뢰가 있으면 어떻게 해야할까요?
                                # 걔는 0이아닌 다른 숫자로 바꿔야합니다.
                                # 지뢰의 갯수가 중요한게 아니니 저히는 럭키 세븐으로 바꾸도록 할게요
                                mat[y][x] = 7
                                break
                        else:
                            for _ in dxdy:
                                if mat[y+_[0]][x+_[1]] == '.':
                                    # 이번엔 지뢰가 아니면 걔를 dq에 넣어야합니다.
                                    # 걔 중심으로 또 돌아야 하기 때문이죠
                                    dq.append([y+_[0],x+_[1]])
                                    mat[y+_[0]][x+_[1]] = 0
    # 자 여기까지 했는데 우리가 빠진게 있죠?
    # 지뢰 주변에 있는 '.' 을 체크 안했어요
    # 걔들은 순회로 조집시다.
    for i in range(1,N+1):
        for j in range(1,N+1):
            if mat[i][j] == '.':
                cnt += 1
    print('#{} {}'.format(tc + 1, cnt))

# 이 문제에서 중요한거는 주변에 지뢰가 있나 없나 먼저 확인을 한 뒤에 그게 아니면 다시 재 확인을 하여 모두가 '.' 이면 큐에 넣어야한다는 점이다.
# 막연히 지뢰 아닌 곳 찾다가 지뢰 찾고 거기서 멈추면 지뢰 아닌 곳을 이미 dq에 넣어버렸으니
# 결과가 꼬여버린다.
# 그리고 패딩 만드는게 은근 편하네 벽 생각 할 필요없이
# 자주 만들도록하자