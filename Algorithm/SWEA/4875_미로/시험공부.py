import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

def DFS(a):
    global result
    for _ in dxdy:
        if 0<=a[0]+_[0]<N and 0<=a[1]+_[1]<N and maze[a[0]+_[0]][a[1]+_[1]]==3:
            result=1
        if 0<=a[0]+_[0]<N and 0<=a[1]+_[1]<N and maze[a[0]+_[0]][a[1]+_[1]]==0:
            y=a[0]+_[0]
            x=a[1]+_[1]
            maze[y][x]=1
            DFS([y,x])
    else:
        return

for tc in range(testcases):
    N=int(input())
    maze=[[0]*N for _ in range(N)]
    dxdy=[(1,0),(0,1),(0,-1),(-1,0)]
    result=0
    for i in range(N):
        x=input()
        for j in range(N):
            maze[i][j]=int(x[j])
            if maze[i][j]==2:
                S=[i,j]
            if maze[i][j]==3:
                G=[i,j]
    DFS(S)
    print('#{} {}'.format(tc+1,result))