import sys
sys.stdin=open('sample_input.txt','r')

def solving(stack, top):
    x=stack[top][1]
    y=stack[top][0]
    for i in range(len(dxdy)):
        if 0<=y+dxdy[i][0]<=N-1 and 0<= x+dxdy[i][1] <=N-1 and maze[y+dxdy[i][0]][x+dxdy[i][1]]==3:
            print(f'#{tc+1} 1')
            return 0
        elif 0<=y+dxdy[i][0]<=N-1 and 0<= x+dxdy[i][1] <=N-1 and maze[y+dxdy[i][0]][x+dxdy[i][1]]==0:
            maze[y + dxdy[i][0]][x + dxdy[i][1]]='-'
            top+=1
            stack[top]=[y + dxdy[i][0], x + dxdy[i][1]]
            solving(stack, top)
    else:

        top-=1


testcases=int(input())
for tc in range(testcases):
    N=int(input())
    state=False
    maze= [[int(i) for i in input()] for j in range(N)]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]==2:
                y=i
                x=j
    stack=['-'] * 10000
    stack[0]=(y,x)
    top = 0
    dxdy=[(-1,0),(0,1),(1,0),(0,-1)]
    solving(stack, top)