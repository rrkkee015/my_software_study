import sys
sys.stdin=open('input.txt','r')

testcases=10

for tc in range(testcases):
    N=int(input())
    matrix = [list(map(int,input().split())) for i in range(100)]
    num3=0
    num4=0
    result = 0
    for i in range(len(matrix)):
        num=0
        num2=0
        num3 += matrix[i][i]
        num4 += matrix[99 - i][i]
        for j in range(len(matrix[i])):
            num += matrix[i][j]
            num2 += matrix[j][i]
        if result < num:
            result = num
        if result < num2:
            result = num2
    if result < num3:
        result = num3
    if result < num4:
        result = num4
    print(f'#{N} {result}')