import sys
sys.stdin=open('input.txt','r')

testcases=10

def up(y,x,tc):
    y-=1
    if y == 0:
        print(f'#{tc} {x}')
    else:
        if x+1<100 and mat[y][x+1] == 1:
            while x+1<100 and mat[y][x+1] == 1:
                x+=1
        elif x-1>=0 and  mat[y][x-1] == 1:
            while x-1>=0 and mat[y][x-1] == 1:
                x-=1
        up(y,x,tc)


for tc in range(testcases):
    tc = int(input())
    mat=[]
    S=[]
    for _ in range(100):
        mat.append(list(map(int,input().split())))
    # for i in mat:
    #     print(i)
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]==2:
                S=[i,j]
                break
        if S:
            break
    up(S[0],S[1],tc)
