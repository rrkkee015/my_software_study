testcases=int(input())
for tc in range(testcases):
    M,N,K=tuple(map(int,input().split()))
    matrix=[[0 for i in range(M)] for j in range(N)]
    for bachu in range(K):
        X,Y=tuple(map(int,input().split()))
        matrix[Y][X]=1
    dxdy=[(0,-1),(1,0),(0,1),(-1,0)]
    cnt=0
    stack=[0 for i in range(K)]
    top=-1
    for i in range(N):
        for j in range(M):
            if matrix[i][j]==1:
                x=j
                y=i
                top+=1
                stack[top]=[i,j]
                matrix[i][j]=2
                while True:
                    for k in dxdy:
                        x=x+k[0]
                        y=y+k[1]
                        if x<0:
                            x=x+1
                            continue
                        elif x>M-1:
                            x=x-1
                            continue
                        elif y<0:
                            y=y+1
                            continue
                        elif y>N-1:
                            y=y-1
                            continue
                        elif matrix[y][x]==1:
                            top+=1
                            stack[top]=[y,x]
                            matrix[y][x]=2
                            break
                        else:
                            x=x-k[0]
                            y=y-k[1]
                    else:
                        matrix[stack[top][0]][stack[top][1]]=0
                        stack[top]=0
                        top-=1
                        if top==-1:
                            cnt += 1
                            break
                        y,x=(stack[top][0],stack[top][1])
    print(cnt)