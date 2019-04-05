import sys
sys.stdin = open('sample_input.txt','r')

testcases = int(input())
for tc in range(testcases):
    # 도시의 크기와 한 가구당 가치를 입력 받습니다.
    N, M = list(map(int,input().split()))
    # 도시 지도를 받습니다.
    mat = [list(map(int,input().split())) for _ in range(N)]
    home = 0
    # 이제 집수를 미리 세봅시다.
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                home += 1
    # 집 수에서 최대로 낼 수 있는 이용비용은 뭘까요?
    maximum = home * M
    # 이걸 왜 구했을 까요??
    # K 가 커질 수록 운영 비용이 기하 급수적으로 커집니다.
    # 그렇다면 그 K가 커질 수 있는 최솟값이 존재하지 않을까요?
    # 모든 집이 이용할 수 있는 범위를 잡아놓고 그래도 회사 입장에서 이익이면 운용을 해도 되지만, 그게 아니라면 K 는 더이상 커지면 안됩니다.
    # 굿?
    K_max = 1
    while K_max * K_max + (K_max - 1) * (K_max - 1) < maximum:
        K_max += 1
    # K는 1부터 시작해서 2*K - 1이 N 보다 작거나 같을 때까지 할 수 있습니다.
    # 근데 문득 드는 생각으로 K가 1 일땐 확인할 필요 없을거 같네요.
    # 그러니 최대 운영 비용은 K가 1일 때로 초기값을 잡겠습니다.
    if M - 1 >= 0:
        max_ = 1
    else:
        max_ = 0
    # 그러면 K가 2일 때부터 확인하면 되겠군요
    K = 2
    # 그리고 또 생각해보니 굳이 전부 돌 필요없이 그 중심으로 모든 좌표에 (i - (K - 1), j - (K - 1)) => (i + (K - 1), j + (K - 1)) 만큼 순회하면 된다.
    while K <= K_max:
        for i in range(N):
            for j in range(N):
                # 처음엔 집을 만나면 방범을 설치하려 했는데, 빈 공터에다가도 방범 시스템을 설치 할  수 있습니다.
                house = 0
                for k in range(i - (K - 1), i + (K - 1) + 1):
                    for p in range(j - (K - 1), j + (K - 1) + 1):
                        # 돌다가 집을 만나면 집에 맡게 카운트를 합시다.
                        if 0 <= k < N and 0 <= p < N and -K+1 <= abs(i-k) + abs(j-p) <= K-1 and mat[k][p] == 1:
                            house += 1
                # 만약 이익이 있으면 그 집 수를 최댓값과 비교합니다.
                if house * M - (K * K + (K - 1) * (K - 1)) >= 0 and house > max_:
                    max_ = house
        K += 1
    print('#{} {}'.format(tc + 1, max_))

