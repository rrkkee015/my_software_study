import sys
sys.stdin = open('input.txt','r')

testcases = int(input())

def cycle(sum_, x, y, cnt):
    global min_
    cnt += 1
    if cnt == N:
        sum_ += abs(x-home[0]) + abs(y-home[1])
        if min_ > sum_:
            min_ = sum_
        return
    if min_ < sum_:
        return
    else:
        for _ in range(N):
            if visited[_] == False:
                visited[_] = True
                xp = gogaek[_][0]
                yp = gogaek[_][1]
                cycle(sum_ + abs(x-xp) + abs(y-yp), xp, yp, cnt)
                visited[_] = False

for tc in range(testcases):
    N = int(input())
    lis_temp = list(map(int,input().split()))
    min_ = 0xfffff
    gogaek = []
    for _ in range(0, len(lis_temp), 2):
        if _ == 0:
            company = (lis_temp[_], lis_temp[_ + 1])
        elif _ == 2:
            home = (lis_temp[_], lis_temp[_ + 1])
        else:
            gogaek.append([lis_temp[_], lis_temp[_ + 1]])
    visited = [False] * N
    cycle(0, company[0], company[1], -1) # 합한 값, 현재 위치, 횟수
    print(f'#{tc+1} {min_}')