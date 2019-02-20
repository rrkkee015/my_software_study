import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

for tc in range(testcases):
    N=int(input())
    maze=[[0 for i in range(N)] for i in range(N)]
    visited=[[False for i in range(N)] for i in range(N)]
    for i in range(N):
        maze_ = input()
        for k in range(len(maze_)):
            maze[i][k]=maze_[k]
            if maze_[k]=='2':
                y=i
                x=k
    dxdy=[(1,0),(0,1),(0,-1),(-1,0)]
    stack=[0]*100
    stack[0]=(y,x)
    top=0
    result=0
    while top!=-1:
        for i in range(len(dxdy)):
            if 0<=y+dxdy[i][0]<=N-1 and 0<=x+dxdy[i][1]<=N-1 and maze[y+dxdy[i][0]][x+dxdy[i][1]]=='3':
                result=1
                break
            elif 0<=y+dxdy[i][0]<=N-1 and 0<=x+dxdy[i][1]<=N-1 and maze[y+dxdy[i][0]][x+dxdy[i][1]]=='0':
                x=x+dxdy[i][1]
                y=y+dxdy[i][0]
                top+=1
                stack[top]=(y,x)
                maze[y][x]='-'
                break
        else:
            maze[y][x]='-'
            stack[top]=0
            top-=1
            y=stack[top][0]
            x=stack[top][1]
        if result==1:
            print(f'#{tc+1} {result}')
            break
    print(f'#{tc+1} 0')