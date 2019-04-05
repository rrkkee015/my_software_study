import sys
sys.stdin = open('sample_input.txt','r')

# dfs 함수
def dfs(i, j, n, num):
    # 만약 자릿수가 7자리가 된다면
    if n == 7:
        # 그 수가 딕셔너리에 없다면 추가
        if num not in result:
            result[num] = 1
        return
    # 만약 자릿수가 7자리를 넘는다면 그 함수는 종료
    elif n > 7:
        return
    # 만약 자릿수가 7자리로 도달 못했으면
    else:
        # 순회를 하면서 자릿수에 넣을 수자를 찾는다.
        for _ in dxdy:
            # 단, 벽을 넘어선 제외
            if 0 <= _[0] + i < 4 and 0 <= _[1] + j < 4:
                dfs(_[0] + i, _[1] + j, n + 1, num + str(mat[_[0] + i][_[1] + j]))
        # 보통 dfs 문제라면 visited를 처리했을텐데 이 문제에서는 그게 없다.
        # 왜냐면 다시 방문이 가능하기 때문

testcases = int(input())
for tc in range(testcases):
    # 결과를 담을 result 딕셔너리
    result = {}
    # 순회를 위한 동서남북 배열
    dxdy = [(0,1),(1,0),(-1,0),(0,-1)]
    # 4x4 행렬을 받는다.
    mat = [list(map(int,input().split())) for _ in range(4)]
    # 4x4 순회를 위해서 visited 행렬도 만든다.
    visited = [[0]*4 for _ in range(4)]
    # visited 행렬 순회를 위해서 행 우선 순회를 사용한다.
    for i in range(4):
        for j in range(4):
            # vistied[i][j]를 방문 안했으면 방문처리를 한다.
            if visited[i][j] == 0:
                visited[i][j] = 1
                # 방문처리를 했으니 이 시작점에서 DFS를 돌린다.
                # 인자로는 시작할 지점과 자릿수와 만들 숫자를 넘긴다.
                dfs(i, j, 0, '')
    print('#{} {}'.format(tc + 1, len(result)))