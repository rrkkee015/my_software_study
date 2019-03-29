import sys
sys.stdin = open('test_2.txt','r')

from itertools import combinations

testcases = int(input())
for tc in range(testcases):
    N, M = list(map(int,input().split())) # N 은 행의크기, M 은 열의크기
    mat = [list(map(int,input().split())) for _ in range(N)]
    max_ = 0
    for s_ in range(1, N):
        s = s_
        for g1_ in range(1, M-1):
            g1 = g1_
            for g2_ in range(g1+1, M):
                g2 = g2_
                t1, t2, t3, t4, t5, t6 = 0, 0, 0, 0, 0, 0
                for i in range(N):
                    for j in range(M):
                        if i < s and j < g1: # 1구역
                            t1 += mat[i][j]
                        elif i < s and g1 <= j < g2: # 2구역
                            t2 += mat[i][j]
                        elif i < s and g2 <= j: # 3구역
                            t3 += mat[i][j]
                        elif s <= i and j < g1: # 4구역
                            t4 += mat[i][j]
                        elif s <= i and g1 <= j < g2: # 5구역
                            t5 += mat[i][j]
                        elif s <= i and g2 <= j: # 6구역
                            t6 += mat[i][j]
                scores = list(combinations([t1, t2, t3, t4, t5, t6], 3))
                for _ in range(len(scores)):
                    score = list(combinations(scores[_], 2))
                    sc = 0
                    for __ in score:
                        a,b = __
                        c = a - b
                        sc+= abs(c)
                    scores[_] = sc
                max_ = max(max_, max(scores))
    print(f'#{tc+1} {max_}')