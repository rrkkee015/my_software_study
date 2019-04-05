import sys
sys.stdin = open('sample_input.txt','r')

import itertools

def honey(slave1, slave2):
    global max_
    # 잠시 노예들의 꿀을 담을 통을 만들었습니다.
    slave1_honey = []
    slave2_honey = []
    # 노예들의 꿀을 통에 넣는 방법을 전부 조합으로 뽑고
    for _ in range(1, work + 1):
        slave1_honey.append(list(itertools.combinations(slave1, _)))
        slave2_honey.append(list(itertools.combinations(slave2, _)))
    slave1_max = 0
    slave2_max = 0
    # 그 중에 최댓값을 뽑을건데
    for _ in slave1_honey:
        for __ in _:
            temp = []
            slave1_result = 0
            for ___ in __:
                temp.append(___)
            # 통에 꿀을 최대로 넣을 수 있는 방법을 찾고
            if c >= sum(temp):
                for ___ in temp:
                    slave1_result += ___**2
            # 그게 노예 1의 최대치의 이익이면 저장을 합니다.
            if slave1_max < slave1_result:
                slave1_max = slave1_result
    # 노예 2도 마찬가지
    for _ in slave2_honey:
        for __ in _:
            temp = []
            slave2_result = 0
            for ___ in __:
                temp.append(___)
            if c >= sum(temp):
                for ___ in temp:
                    slave2_result += ___**2
            if slave2_max < slave2_result:
                slave2_max = slave2_result
    # 그 두 개 더한게 전체 다해서 최댓값인지 확인하고 저장합니다.
    if max_ < slave1_max + slave2_max:
        max_ = slave1_max + slave2_max

testcases = int(input())
for tc in range(testcases):
    # 벌통의 사이즈, 일꾼이 채취할 수 있는 가로길이, 담을 수 있는 통의 크기
    size, work, c = list(map(int,input().split()))
    honey_house = [list(map(int,input().split())) for _ in range(size)]
    max_ = 0

    # 순회를 해야겠죠, 근데 순회가 애매한게 계속 돌려야합니다. 1번 2번 일꾼으로 이름을 지을게요.
    # 1번 일꾼이 고정하고, 2번 일꾼이 돌아다니고, 다 돌았으면 1번 일꾼 옆으로 이동하고 이런 식으로 해야할 거 같네요.
    # 그렇다면 for 문을 1번을 위한 for문 2번을 위한 for문을 만들면 좋겠넹요
    # 요게 1번을 위한 for 문
    for i in range(size - 1):
        for j in range(size - work + 1):
            slave_1 = honey_house[i][j:j + work]
            # 요게 2번을 위한 for 문입니다.
            # 근데요, 이게 노예들이 일하는 범위에 따라서 같은 행에서 일하는 방법이 달라집니다.
            # 만약, 선택할 수 있는 벌통의 가로길이 * 2가 N 보다 크면 그 행은 한 사람이 독차지가 가능합니다.
            if work * 2 > size :
                for y in range(i + 1 , size):
                    for x in range(size):
                        # 그럼 여기서 2번 일꾼의 범위를 잡아주면 되겠죠?
                        # 만약 일을 제대로 못하면 다시 시켜야합니다.
                        if len(honey_house[y][x:x + work]) < work:
                            continue
                        else:
                            slave_2 = honey_house[y][x:x + work]
                            honey(slave_1, slave_2)
            # 그게 아니면 또 공유를 할 수 있어요. 같은 행에서 말이죠
            else:
                for y in range(i, size):
                    if i == y:
                        for x in range(j + work, size):
                            if i == y:
                                if len(honey_house[y][x:x + work]) == work:
                                    slave_2 = honey_house[y][x:x + work]
                                    honey(slave_1, slave_2)
                    else:
                        for x in range(size - work + 1):
                            slave_2 = honey_house[y][x:x + work]
                            honey(slave_1, slave_2)
    print('#{} {}'.format(tc + 1, max_))

# 어떻게 하면 시간을 줄일까?