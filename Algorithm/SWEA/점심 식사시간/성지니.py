# 완성 직전 9번만 틀림
import sys, collections

sys.stdin = open("sample_input.txt", "r")


def first_time(first_stair):  # 1번 계단으로 가는 사람들의 좌표정보를 담은 배열을 넘긴다.
    first_one = stairs[0]  # 1번 계단의 좌표정보 + 계단 높이
    height = first_one[2]  # 계단 높이
    arrival = collections.deque()  # 1번 계단으로 가는 사람들의 도착시간을 담을 배열
    for idx in range(len(first_stair)):
        people = first_stair[idx]  # 사람마다
        d = abs(people[0] - first_one[0]) + abs(people[1] - first_one[1])  # 계단 까지의 거리 계산
        arrival.append(d)
    # 도착 시간을 받아왔으면 정렬
    arrival = sorted(arrival)
    # 계단 내려가는 마음의 준비
    for _ in range(len(arrival)):
        arrival[_] += 1
    print(arrival)
    # 계단 내려갑니다.
    # 공집합은 볼 필요없단다 ㅎ
    if arrival == []:
        return 0
    # 만약 사람 수가 3명보다 작으면 제일 늦게 온 놈이 나쁜 놈이야.
    elif len(arrival) <= 3:
        # 얘가 제일 늦은 애 어차피 계단에 제일 늦게 오는 애가 제일 늦게 내려가니까
        max_late_1 = arrival[-1] + height
    else: # 별표 3 개
        # 계단에 도착한 앞에서 3명은 바로 계단을 이용한다.
        for _ in range(3):
            arrival[_] += height
        # 그 뒤에 4번째 애부터는 비교를 해야한다.
        # 왜냐면 기다릴 수도 있고 계단을 도착한 시간보다 더 늦게와서 바로 내려갈 수 있기 때문에
        # 두 값을 비교해서 더 큰 값을 이용하여 시간을 재야한다.
        # 알겠니
        # 성지나
        for _ in range(3, len(arrival)):
            arrival[_] = max(arrival[_], arrival[_ - 3]) + height
        max_late_1 = arrival[-1]
    return max_late_1

# 2번도 똑같이
def second_time(second_stair):
    second_one = stairs[1]
    height = second_one[2]
    arrival = collections.deque()
    for idx in range(len(second_stair)):
        people = second_stair[idx]
        d = abs(people[0] - second_one[0]) + abs(people[1] - second_one[1])
        arrival.append(d)
    arrival = sorted(arrival)
    for _ in range(len(arrival)):
        arrival[_] += 1
    if arrival == []:
        return 0
    elif len(arrival) <= 3:
        max_late_1 = arrival[-1] + height
    else:
        for _ in range(3):
            arrival[_] += height
        for _ in range(3, len(arrival)):
            arrival[_] = max(arrival[_], arrival[_ - 3]) + height
        max_late_1 = arrival[-1]
    return max_late_1


T = int(input())
for t in range(1, T + 1):
    # input
    n = int(input())
    mapp = [0 for _ in range(n)]
    for _ in range(n):
        mapp[_] = list(map(int, input().split()))

    # 사전조사
    people = collections.deque()  # 사람 좌표들
    stairs = collections.deque()  # 계단 좌표들
    for _ in range(n):
        for __ in range(n):
            if mapp[_][__] == 1:
                people.append((_, __))  # 사람이면 좌표 넣어주고.
            if 2 <= mapp[_][__] <= 10:  # 계단이면
                stairs.append((_, __, mapp[_][__]))
    p_n = len(people)  # 사람수 따로 저장

    # 사람 쪼개고 시간 구하는 것까지 해보자. 사람 쪼개는 건 부분집합 이용해서
    minn = 0xfffffff
    for i in range(1 << p_n):  # 각각의 결정집합 마다
        first_stair = collections.deque()
        second_stair = collections.deque()
        for j in range(p_n):
            if i & (1 << j):  # 1인 경우 first 계단에 추가
                first_stair.append(people[j])
            else:  # 0인 경우 second 계단에 추가
                second_stair.append(people[j])

        # 여기서 구현
        ft = first_time(first_stair)
        st = second_time(second_stair)

        if max(ft,st) < minn:
            minn = max(ft,st)
    print("#{} {}".format(t, minn))




