import sys
sys.stdin = open('sample_input.txt','r')

import itertools

testcases = int(input())

for tc in range(testcases):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    temp_mat = [_ for _ in range(N)]
    cobi = list(itertools.combinations(temp_mat, N//2))
    min_ = 0xffffff
    for _ in range(len(cobi)//2):
        cook1 = 0
        cook2 = 0
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                cook1 += mat[cobi[_][i]][cobi[_][j]] + mat[cobi[_][j]][cobi[_][i]]
                cook2 += mat[cobi[-1-_][i]][cobi[-1-_][j]] + mat[cobi[-1-_][j]][cobi[-1-_][i]]
        if min_ > abs(cook1-cook2):
            min_ = abs(cook1-cook2)
    print(f'#{tc+1} {min_}')