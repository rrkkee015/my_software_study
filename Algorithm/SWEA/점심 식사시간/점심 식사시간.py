import sys
sys.stdin = open('sample_input.txt','r')

import itertools

testcases = int(input())

def comb(cnt): # 중복조합
    if cnt == len(people):
        time1 = []
        time2 = []
        for _ in range(len(visited)):
            if visited[_] == 1:
                time1.append(stair1[_])
            elif visited[_] == 2:
                time2.append(stair2[_])
        stair1_t.append(time1)
        stair2_t.append(time2)
        return
    visited[cnt] = 1
    comb(cnt+1)
    visited[cnt] = 2
    comb(cnt+1)

for tc in range(testcases):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    result = []

    # 사람들의 좌표와 계단의 좌표를 알아냅시다.
    people = []
    stairs = []
    stairs_heghit = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                people.append([i, j])
            elif 2 <= mat[i][j] <= 10:
                stairs.append([i, j])
                stairs_heghit.append(mat[i][j])

    # 사람과 계단들을 번호로 부르기 위해서 인덱스에 맞도록 설정합니다.
    people = [0] + people
    stairs = [0] + stairs
    stairs_heghit = [0] + stairs_heghit
    # 계단 1에 가는 시간
    stair1 = [0 for _ in range(len(people))]
    # 계단 2에 가는 시간
    stair2 = [0 for _ in range(len(people))]
    for _ in range(1, len(people)):
        stair1[_] = abs(people[_][0] - stairs[1][0]) + abs(people[_][1] - stairs[1][1])
        stair2[_] = abs(people[_][0] - stairs[2][0]) + abs(people[_][1] - stairs[2][1]) # 여기까진 문제 없습니다.

    # 사람 수에 따른 계단 1에 도달하는 경우의 수
    # 사람 수에 따른 계단 2에 도달하는 경우의 수
    stair1_t = []
    stair2_t = []
    # 라이브러리를 쓰면 사람 1, 2, 3, 4, 5, 6 중에 누가 1번 계단으로 갔는지 누가 2번 계단으로 갔는지 알 수가 없다.
    # for _ in range(len(people)):
    #     stair1_t.append(list(itertools.combinations(stair1[1:], _)))
    # for _ in range(len(people) - 1, -1, -1):
    #     stair2_t.append(list(itertools.combinations(stair2[1:], _)))
    visited = [0] * len(people)
    comb(1) # 여기까지도 문제가 없습니다.

    # 사람 수에 따른 계단 도달 한 시간을 짝에 맞게 설정합니다.
    for _ in range(len(stair1_t)):
        front_stair1 = sorted(list(stair1_t[_]))
        front_stair2 = sorted(list(stair2_t[_]))
        print(front_stair1)
        # 계단 앞에 도착했으니 전부 1을 더합니다.
        for ___ in range(len(front_stair1)):
            front_stair1[___] = front_stair1[___] + 1
        for ___ in range(len(front_stair2)):
            front_stair2[___] = front_stair2[___] + 1
        # 이제 계단을 내려갑니다.
        # 만약 계단을 기다리는 사람이 3명 이하면 그냥 다 보내고 최댓값을 뽑는다.
        # 1번 계단에 서있는 사람부터 처리합시다.
        if  front_stair1 == []:
            max_front_stair1 = 0
        elif len(front_stair1) <= 3:
            max_front_stair1 = max(front_stair1) + stairs_heghit[1]
        else:
            # 우선 앞에 있는 사람들은 계단을 보냅니다.
            for ___ in range(3):
                front_stair1[___] += stairs_heghit[1]
            # 그 뒤부터는 전 전 전 사람과 비교해서 더 큰 값에다가 숫자를 더해서 채워 갑니다.
            for ___ in range(3, len(front_stair1)):
                front_stair1[___] = max(front_stair1[___ - 3], front_stair1[___]) + stairs_heghit[1]
            max_front_stair1 = front_stair1[-1]
        # 2번 계단에 서있는 사람을 처리합니다.
        if front_stair2 == []:
            max_front_stair2 = 0
        elif len(front_stair2) <= 3:
            max_front_stair2 = max(front_stair2) + stairs_heghit[2]
        else:
            for ___ in range(3):
                front_stair2[___] += stairs_heghit[2]
            for ___ in range(3, len(front_stair2)):
                front_stair2[___] = max(front_stair2[___ - 3], front_stair2[___]) + stairs_heghit[2]
            max_front_stair2 = front_stair2[-1]
        # 둘 중 큰 값을 넣습니다.
        result.append(max(max_front_stair1, max_front_stair2))
    # 결과는 최댓값 중 최솟값을 뽑습니다.
    print('#{} {}'.format(tc + 1, min(result)))