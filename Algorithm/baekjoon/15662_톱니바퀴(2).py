T = int(input())
wheel = [[] for _ in range(T)]
for _ in range(T):
    temp = input()
    for __ in temp:
        wheel[_].append(int(__))
K = int(input())
result = 0

for _ in range(K):
    # 회전 방향 정하기
    wh_d = [0 for t in range(T)]
    num, d = map(int,input().split())
    num -= 1
    wh_d[num] = d
    # 왼쪽
    l = num
    temp_d = d
    while l-1 != -1:
        l -= 1
        if wheel[l][2] != wheel[l + 1][6]:
            temp_d *= -1
            wh_d[l] = temp_d
        else:
            break
    # 오른쪽
    r = num
    temp_d = d
    while r + 1 != T:
        r += 1
        if wheel[r][6] != wheel[r - 1][2]:
            temp_d *= -1
            wh_d[r] = temp_d
        else:
            break
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
        result += 1
print(result)