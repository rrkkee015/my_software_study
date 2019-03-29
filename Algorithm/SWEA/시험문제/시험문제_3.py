import sys
sys.stdin = open('test_3.txt','r')
import collections, time

def permutaion(depth, cnt):
    global min_
    depth += 1
    if depth == N:
        if min_ > cnt:
            min_ = cnt
        return
    elif cnt > min_:
        return
    else:
        for _ in range(N):
            if visited[_]:
                visited[_] = False
                permutaion(depth, cnt + result[depth][_])
                visited[_] = True

testcases = int(input())
for tc in range(testcases):
    N = int(input())
    chips = list(map(int,input().split()))
    robots = list(map(int,input().split()))
    robots_cnt = len(robots)//2
    eating = collections.deque()
    min_ = 0xffffff

    max_mat = max(max(chips), max(robots)) + 1

    dxdy = [(0,1),(1,0),(-1,0),(0,-1)]
    result = []
    for _ in range(0, robots_cnt*2, 2):
        mat = [[0] * max_mat for _ in range(max_mat)]
        temp_result = [0] * N
        snack_number = 1
        for __ in range(0, len(chips), 2):
            mat[chips[__]][chips[__ + 1]] = snack_number # 과자는 과자 번호로 한다
            snack_number += 1
        eating.append([robots[_], robots[_ + 1], 0]) #로봇의 위치와 걔가 먹은 과자 갯수
        mat[robots[_]][robots[_ + 1]] = -1
        while eating:
            y, x , cnt = eating.popleft()
            for _ in dxdy:
                if 0 <= y + _[0] < max_mat and 0 <= x + _[1] < max_mat and mat[y + _[0]][x + _[1]] != -1:
                    if mat[y + _[0]][x + _[1]] != 0:
                        temp_result[mat[y + _[0]][x + _[1]] -1] = cnt + 1
                        mat[y + _[0]][x + _[1]] = -1
                        eating.append([y + _[0], x + _[1], cnt + 1])
                    else:
                        mat[y + _[0]][x + _[1]] = -1
                        eating.append([y + _[0], x + _[1], cnt + 1])
        result.append(temp_result)

    visited = [True] * len(result)
    permutaion(-1, 0)
    print(f'#{tc+1} {min_}')