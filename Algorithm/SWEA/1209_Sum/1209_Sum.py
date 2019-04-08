import sys
sys.stdin = open('input.txt','r')

for tc in range(10):
    tc = int(input())
    mat = [list(map(int,input().split())) for _ in range(100)]
    sum = []
    sum3 = 0
    sum4 = 0
    for i in range(100):
        sum1 = 0
        sum2 = 0
        for j in range(100):
            if i == j:
                sum3 += mat[i][j]
            if i + j == 99:
                sum4 += mat[i][j]
            sum1 += mat[i][j]
            sum2 += mat[j][i]
        sum.append(sum1)
        sum.append(sum2)
    sum.append(sum3)
    sum.append(sum4)
    print('#{} {}'.format(tc, max(sum)))