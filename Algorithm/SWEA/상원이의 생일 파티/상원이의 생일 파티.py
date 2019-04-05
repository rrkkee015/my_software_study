import sys
sys.stdin = open('input.txt','r')

# 상원이의 친구와 그 친구의 친구까지 초대장을 뿌린다. 그렇다면 과연 몇 명이 초대장을 받을까?
import collections

testcases = int(input())
for tc in range(testcases):
    # 사람 수 N, 친구 관계 M
    N, M = list(map(int,input().split()))

    # 관계 지도 설정
    mat = [[0]*(N + 1) for _ in range(N + 1)]
    for _ in range(M):
        s, g = list(map(int,input().split()))
        mat[s][g] = 1
        mat[g][s] = 1

    # BFS를 사용해서 깊이가 2까지 되는 친구들까지만 초대 하겠다.
    dq = collections.deque()
    visited = [True] * (N + 1)
    visited[0] = False
    # 참고로 상원이는 깊이가 0 이다.
    dq.append([1, 0])
    visited[1] = False
    cnt = 0

    while dq:
        p, depth = dq.popleft()
        depth += 1
        if depth == 3:
            break
        for _ in range(len(mat)):
            if mat[p][_] == 1 and visited[_]:
                visited[_] = False
                dq.append([_, depth])
                cnt += 1
    print('#{} {}'.format(tc + 1, cnt))