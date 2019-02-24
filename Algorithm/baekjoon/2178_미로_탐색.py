def search(y,x,cnt):
    if y==N-1 and x==M-1:
        print(cnt)
    else:
        for k in dxdy:
            if 0<=y+k[0]<=N-1 and 0<=x+k[1]<=M-1 and Ma[y+k[0]][x+k[1]]==1:
                Ma[y+k[0]][x+k[1]]=0
                cnt+=1
                search(y+k[0],x+k[1],cnt)

N,M=tuple(map(int,input().split()))
Ma=[[int(i) for i in input()] for j in range(N)]
cnt=0
dxdy=[(1,0),(0,-1),(-1,0),(0,1)]
Ma[0][0]=0
cnt+=1
search(0,0,cnt)
