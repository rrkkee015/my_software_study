wheel = [[] for _ in range(4)]
for _ in range(4):
    temp = input()
    for __ in temp:
        wheel[_].append(int(__))
K = int(input())
result = 0

for _ in range(K):
    # 회전 방향 정하기
    wh_d = [0, 0, 0, 0]
    num, d = map(int,input().split())
    num -= 1
    if num == 0:
        wh_d[0] = d
        if wheel[0][2] != wheel[1][6]:
            wh_d[1] = d * (-1)
            if wheel[1][2] != wheel[2][6]:
                wh_d[2] = d
                if wheel[2][2] != wheel[3][6]:
                    wh_d[3] = d * (-1)
    elif num == 1:
        wh_d[1] = d
        if wheel[1][6] != wheel[0][2]:
            wh_d[0] = d * (-1)
        if wheel[1][2] != wheel[2][6]:
            wh_d[2] = d * (-1)
            if wheel[2][2] != wheel[3][6]:
                wh_d[3] = d
    elif num == 2:
        wh_d[2] = d
        if wheel[2][2] != wheel[3][6]:
            wh_d[3] = d * (-1)
        if wheel[2][6] != wheel[1][2]:
            wh_d[1] = d * (-1)
            if wheel[1][6] != wheel[0][2]:
                wh_d[0] = d
    elif num == 3:
        wh_d[3] = d
        if wheel[3][6] != wheel[2][2]:
            wh_d[2] = d * (-1)
            if wheel[2][6] != wheel[1][2]:
                wh_d[1] = d
                if wheel[1][6] != wheel[0][2]:
                    wh_d[0] = d * (-1)
    # 회전하기
    for go in range(len(wh_d)):
        visited = [0 for _ in range(8)]
        if wh_d[go] != 0:
            if wh_d[go] == 1:
                temp = wheel[go][-1]
                for __ in range(len(wheel[go]) - 1):
                    visited[__ + 1] = wheel[go][__]
                visited[0] = temp
            else:
                temp = wheel[go][0]
                for __ in range(len(wheel[go]) - 1, 0, -1):
                    visited[__ - 1] = wheel[go][__]
                visited[-1] = temp
            wheel[go] = visited

for _ in range(len(wheel)):
    if wheel[_][0] == 1:
        result += 2 ** _

print(result)