import sys
sys.stdin = open('sample_input.txt','r')

def choiso(depth, cnt):
    global min_
    depth += 1
    if depth == N:
        if min_ > cnt:
            min_ = cnt
    if cnt > min_:
        return
    for _ in range(N):
        if visited[_]:
            visited[_] = False
            choiso(depth, cnt + mat[depth][_])
            visited[_] = True

testcases = int(input())
for tc in range(testcases):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    visited = [True] * N
    min_ = 0xffffff
    choiso(-1, 0)
    print(f'#{tc+1} {min_}')