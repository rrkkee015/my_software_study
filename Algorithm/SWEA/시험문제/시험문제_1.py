import sys
sys.stdin = open('test_1.txt','r')
import collections

testcases = int(input())
for tc in range(testcases):
    N = int(input()) # 장기판 크기 10 <= N <= 20
    sy, sx, gy, gx = list(map(int,input().split())) # 장기 초기 위치, 장기 목표 위치
    mat = [[0] * N for _ in range(N)]
    mat[sy][sx] = 1
    dq = collections.deque()
    dq.append([sy,sx,0])
    dxdy = [(2,3), (2,-3), (-2,3), (-2,-3), (3,2), (3,-2), (-3,2), (-3,-2)]
    while dq:
        temp = dq.popleft()
        y = temp[0]
        x = temp[1]
        cnt = temp[2]
        if x == gx and y == gy:
            print(f'#{tc+1} {cnt}')
            break
        for _ in dxdy:
            if 0 <= y + _[0] < N and 0 <= x + _[1] < N and mat[y + _[0]][x + _[1]] != 1:
                mat[y + _[0]][x + _[1]] = 1
                temp = dq.append([y + _[0], x + _[1], cnt+1])