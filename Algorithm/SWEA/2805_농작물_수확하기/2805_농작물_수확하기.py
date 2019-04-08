import sys
sys.stdin = open('input.txt','r')

testcases = int(input())
for tc in range(testcases):
    N = int(input())
    mat = [input() for _ in range(N)]
    depth = 0
    cnt = 0
    # 절반의 순회로 총 합을 구할 수 있다 (대칭이니까)
    for i in range(N//2 + 1):
        for j in range(N//2 - depth, N//2 + 1 + depth):
            if i == N//2:
                cnt += int(mat[i][j])
            else:
                cnt += int(mat[i][j])
                cnt += int(mat[N-1-i][j])
        depth += 1
    print('#{} {}'.format(tc + 1, cnt))