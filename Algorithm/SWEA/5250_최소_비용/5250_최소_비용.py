import sys
sys.stdin = open('sample_input.txt','r')

import collections

testcases = int(input())

for tc in range(testcases):
    N= int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]

    visited = [[0xffff]*N for _ in range(N)]
    visited[0][0] = 0
    dq = collections.deque()
    dxdy = [(0,1),(1,0),(-1,0),(0,-1)]
    dq.append([0,0])
    while dq:
        y, x = dq.popleft()
        for _ in dxdy:
            if 0<=y+_[0]<N and 0<=x+_[1]<N:
                # 오르막
                if mat[y+_[0]][x+_[1]] > mat[y][x]:
                    temp = mat[y+_[0]][x+_[1]] - mat[y][x] + 1 + visited[y][x]
                    if temp >= visited[y+_[0]][x+_[1]]:
                        continue
                    else:
                        visited[y+_[0]][x+_[1]] = temp
                        dq.append([y+_[0],x+_[1]])
                # 내리막
                else:
                    temp = visited[y][x] + 1
                    if temp >= visited[y+_[0]][x+_[1]]:
                        continue
                    else:
                        visited[y+_[0]][x+_[1]] = temp
                        dq.append([y+_[0],x+_[1]])
    for _ in visited:
        print(_)
    print(f'#{tc+1} {visited[-1][-1]}')