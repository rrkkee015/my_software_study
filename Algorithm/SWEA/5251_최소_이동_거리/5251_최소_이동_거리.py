import sys
sys.stdin = open('sample_input.txt','r')

import collections

testcases = int(input())
for tc in range(testcases):
    N, E = list(map(int,input().split()))
    V = [_ for _ in range(N+1)]
    route = [[0]*(N+1) for _ in range(N+1)]
    dis = [0xffff] * (N + 1)
    dis[0] = 0
    for _ in range(E):
        s, g, fee = list(map(int,input().split()))
        route[s][g] = fee
    dq = collections.deque()
    dq.append(0)
    while dq:
        x = dq.pop()
        for _ in range(len(route)):
            if route[x][_] != 0:
                if route[x][_] + dis[x] > dis[_]:
                    continue
                else:
                    dis[_] = min(route[x][_] + dis[x], dis[_])
                    dq.append(_)
    print(f'#{tc+1} {dis[-1]}')
