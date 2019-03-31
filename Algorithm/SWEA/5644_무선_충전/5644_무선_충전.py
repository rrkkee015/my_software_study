import sys
sys.stdin = open('sample_input.txt','r')

def move(y, x, type): # 애들을 움직이자
    if type == 0: # 0일 때 제자리
        return (y, x)
    elif type == 1: # 1일 때 업
        return (y - 1, x)
    elif type == 2: # 2일 때 오른쪽
        return (y, x + 1)
    elif type == 3: # 3일 때 다운
        return (y + 1, x)
    elif type == 4: # 4일 때 왼쪽
        return (y, x - 1)

testcases = int(input())

for tc in range(testcases):
    M, A = list(map(int,input().split()))
    move_A = list(map(int,input().split()))
    move_B = list(map(int,input().split()))

    mat = [[0] * 10 for _ in range(10)] # 파워 체크 지도

    for _ in range(A):
        x, y, c, p = list(map(int,input().split())) # 기지국 x, y 좌표, 기지국 범위, 기지국 파워
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if abs(i - y + 1) + abs(j - x + 1) <= c: # 기지국 범위에 포함되면 아래 수행
                    if mat[i][j] == 0: # 만약 허허벌판이면
                        mat[i][j] = [[_, p]] # 그 기지국의 이름과, 기지국의 파워를 넣는다.
                    else: # 이미 기지국이 있다면
                        mat[i][j] += [[_, p]] # 새로운 애를 추가한다.
                        if len(mat[i][j]) >= 2: # 근데 그게 2개 이상이되버리면 정렬을 하는데
                            mat[i][j] = [sorted(mat[i][j], key = lambda x : x[1])[-2], sorted(mat[i][j], key = lambda x : x[1])[-1]]
                            # 제일 큰 놈 2명만 남기고 나머지는 다 버린다. 파워 기준으로 정렬한다.
    AP = (0,0) # A 초기 위치
    BP = (9,9) # B 초기 위치
    result_A = 0 # A의 결과값
    result_B = 0 # B의 결과값
    t = 0 # 시간
    while t != M + 1: # M + 1 이라곤 했지만 안에서 M 일 때 수행시키고 break를 걸어줘야한다.
        # A, B 둘다 충전소가 아니다.
        if mat[AP[0]][AP[1]] == 0 and mat[BP[0]][BP[1]] == 0 and t != M: # break 조건도 같이 걸어줘야한다.
            # 둘 다 충전소가 아니면 그냥 가던 길 가자
            AP = move(AP[0], AP[1], move_A[t])
            BP = move(BP[0], BP[1], move_B[t])
            t += 1
            continue
        # 한 명만 충전소면 걔 위치에서 가장 큰 충전소의 파워를 추가한다.
        # A는 충전소, B는 아무것도 아님
        if mat[AP[0]][AP[1]] != 0 and mat[BP[0]][BP[1]] == 0:
            result_A += mat[AP[0]][AP[1]][-1][1]
        # B는 충전소, A는 아무것도 아님
        if mat[AP[0]][AP[1]] == 0 and mat[BP[0]][BP[1]] != 0:
            result_B += mat[BP[0]][BP[1]][-1][1]
        # 둘 다 충전소면 경우가 많이 나뉜다. 충전소 갯수 기준으로 1,1 / 1,2 / 2,1 / 2,2 로 나뉜다. 2,2 일땐 또 경우가 나뉘는 데 밑에서 확인하자
        # 둘 다 충전소
        if mat[AP[0]][AP[1]] != 0 and mat[BP[0]][BP[1]] != 0:
            # 둘 다 충전소인데 A는 충전기 한 대고 B도 충전기 한 대이다.
            if len(mat[AP[0]][AP[1]]) == 1 and len(mat[BP[0]][BP[1]]) == 1:
                # 두 개가 공유하면 파워를 나눠서 넣는다.
                if mat[AP[0]][AP[1]][0][0] == mat[BP[0]][BP[1]][0][0]:
                    result_A += mat[AP[0]][AP[1]][0][1] // 2
                    result_B += mat[BP[0]][BP[1]][0][1] // 2
                # 두 개가 공유 안하면 파워를 원본으로 넣는다.
                else:
                    result_A += mat[AP[0]][AP[1]][0][1]
                    result_B += mat[BP[0]][BP[1]][0][1]
            # 둘 다 충전소인데 A는 충전기가 한 대이고 B는 2 대이다. # 이 경우엔 교집합을 가진 애가 양보를 해줘야 A + B의 최댓값이 완성된다. 뺏어가면 한 명은 충전 못하니까
            if len(mat[AP[0]][AP[1]]) == 1 and len(mat[BP[0]][BP[1]]) == 2:
                # 공유하는 충전기가 있으면 B가 겹치는 파워를 A에게 준다.
                for _ in mat[BP[0]][BP[1]]:
                    if mat[AP[0]][AP[1]][0][0] in _:
                        result_A += mat[AP[0]][AP[1]][0][1]
                        result_B += mat[BP[0]][BP[1]][-1][1] + mat[BP[0]][BP[1]][-2][1] - mat[AP[0]][AP[1]][0][1]
                        break
                else: # 공유하는 충전기가 없으면 서로 각자 큰 값을 가져간다.
                    result_A += mat[AP[0]][AP[1]][0][1]
                    result_B += mat[BP[0]][BP[1]][-1][1]
            # 둘 다 충전소인데 A는 충전기가 2 대이고 B는 1 대이다.
            if len(mat[AP[0]][AP[1]]) == 2 and len(mat[BP[0]][BP[1]]) == 1:
                # 공유하는 충전기가 있으면, A가 겹치는 파워를 B에게 준다.
                for _ in mat[AP[0]][AP[1]]:
                    if mat[BP[0]][BP[1]][0][0] in _:
                        result_B += mat[BP[0]][BP[1]][0][1]
                        result_A += mat[AP[0]][AP[1]][-1][1] + mat[AP[0]][AP[1]][-2][1] - mat[BP[0]][BP[1]][0][1]
                        break
                else:
                    result_A += mat[AP[0]][AP[1]][-1][1]
                    result_B += mat[BP[0]][BP[1]][0][1]
            # 둘 다 충전소인데 A도 충전기 2 대이고 B도 2 대이다. # 여기선 공유하는 충전기가 0 대인지, 1 대인지, 2대인지를 고민해야한다.
            if len(mat[AP[0]][AP[1]]) == 2 and len(mat[BP[0]][BP[1]]) == 2:
                cnt = 0 # 공유하는 충전기의 갯 수
                # 공유하는 충전기가 있으면, 1개인지 2개인지 파악
                for _ in mat[AP[0]][AP[1]]:
                    for __ in mat[BP[0]][BP[1]]:
                        if _[0] == __[0]:
                            cnt += 1
                # 공유하는 충전기가 없으면 각자의 최댓값을 더한다.
                if cnt == 0:
                    result_A += mat[AP[0]][AP[1]][-1][1]
                    result_B += mat[BP[0]][BP[1]][-1][1]
                # 공유하는 충전기가 2 대면 result_A 에는 큰 값, result_B 에는 작은 값을 넣는다.
                # result_A, result_B 각각의 값을 원하는 것이 아니기 때문에 이렇게 해도 된다.
                elif cnt == 2:
                    result_A += mat[AP[0]][AP[1]][-1][1]
                    result_B += mat[BP[0]][BP[1]][-2][1]
                else: # 공유하는 충전기가 1 대면 또 경우가 나뉜다. 제일 쎈 파워를 서로가 같이 공유하는 경우 / 각자의 쎈 충전기가 서로 다른 경우
                    # 만약 서로의 최댓값이 같으면 서로의 두 번째 값을 비교해서 결과값이 제일 크게 만들 수 있게 조정해야한다.
                    if mat[AP[0]][AP[1]][-1][1] == mat[BP[0]][BP[1]][-1][1]:
                        # 두 번째 값을 비교해서 넣는다.
                        # 두 번째 값에서 A것이 더 크면 최댓값을 B에 양보
                        if mat[AP[0]][AP[1]][-2][1] > mat[BP[0]][BP[1]][-2][1]:
                            result_A += mat[AP[0]][AP[1]][-2][1]
                            result_B += mat[BP[0]][BP[1]][-1][1]
                        else: # 두 번째 값에서 B것이 더 크면 최댓값을 A에게 양보
                            result_A += mat[AP[0]][AP[1]][-1][1]
                            result_B += mat[BP[0]][BP[1]][-2][1]
                    # 만약 서로의 최댓값이 다르다면 각자 최댓값을 넣으면 된다.
                    if mat[AP[0]][AP[1]][-1][1] != mat[BP[0]][BP[1]][-1][1]:
                        result_A += mat[AP[0]][AP[1]][-1][1]
                        result_B += mat[BP[0]][BP[1]][-1][1]
        if t == M:
            break
        AP = move(AP[0], AP[1], move_A[t])
        BP = move(BP[0], BP[1], move_B[t])
        t += 1
    # if mat[AP[0]][AP[1]] != 0:
    #     result_A += mat[AP[0]][AP[1]][-1][1]
    # if mat[BP[0]][BP[1]] != 0:
    #     result_B += mat[BP[0]][BP[1]][-1][1]
    # 여기서 굳이 내가 while 문을 M + 1을 한 이유가 나온다.
    # 마지막에 처리를 해버리면 최종 도착지에서 겹치는 경우가 있기 때문에 while 문으로 제작한 함수를 또 수행을 시켜야한다.
    print(f'#{tc + 1} {result_A + result_B}')