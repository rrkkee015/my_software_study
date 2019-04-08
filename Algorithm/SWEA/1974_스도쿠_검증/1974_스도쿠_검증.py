import sys
sys.stdin = open('input.txt','r')

testcases = int(input())
for tc in range(testcases):
    mat = [list(map(int,input().split())) for _ in range(9)]
    tt = []
    for _ in range(0,7,3):
        for __ in range(0,7,3):
            tt.append((_,__))
    tf = [0 for _ in range(10)]
    tf[0] = 1
    gon = 1
    for i in range(9):
        m = tf[:]
        I = tf[:]
        for j in range(9):
            m[mat[i][j]] = 1
            I[mat[j][i]] = 1
            if (i,j) in tt:
                s = tf[:]
                for p in range(i, i + 3):
                    for k in range(j, j + 3):
                        s[mat[p][k]] = 1
        if 0 in m or 0 in I or 0 in s:
            gon = 0
            break
    else:
        print('#{} {}'.format(tc + 1, gon))
    if gon == 0:
        print('#{} {}'.format(tc + 1, gon))