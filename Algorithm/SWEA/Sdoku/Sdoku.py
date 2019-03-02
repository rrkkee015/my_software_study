import sys
sys.stdin=open('input.txt','r')

testcases=int(input())

for tc in range(testcases):
    mat=[list(map(int,input().split())) for _ in range(9)]
    error=False
    #행 탐색
    for i in range(9):
        sdoku=[False]*10
        for j in range(9):
            if sdoku[mat[i][j]]==False:
                sdoku[mat[i][j]]=True
            else:
                error=True
                break
    if error==True:
        print(f'#{tc+1} 0')
        continue
    #열 탐색
    for i in range(9):
        sdoku=[False]*10
        for j in range(9):
            if sdoku[mat[j][i]]==False:
                sdoku[mat[j][i]]=True
            else:
                error=True
                break
    if error==True:
        print(f'#{tc+1} 0')
        continue
    #3칸씩 탐색
    for i in range(0,9,3):
        for j in range(0,9,3):
            sdoku=[False]*10
            for y in range(3):
                for x in range(3):
                    if sdoku[mat[i+y][j+x]]==False:
                        sdoku[mat[i+y][j+x]]=True
                    else:
                        error=True
                        break
    if error==True:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} 1')