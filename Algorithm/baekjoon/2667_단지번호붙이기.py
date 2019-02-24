def search(y,x):
    global cnt
    for k in dxdy:
        if (0<=y+k[0]<=N-1 and 0<=x+k[1]<=N-1) and Ma[y+k[0]][x+k[1]]==1:
            Ma[y+k[0]][x+k[1]]=0
            cnt+=1
            search(y+k[0],x+k[1])


N=int(input())
Ma=[[int(i) for i in input()] for j in range(N)]
dxdy=[(1,0),(0,-1),(-1,0),(0,1)]
cnt=0
cnt_=0
result=[]
for i in range(N):
    for j in range(N):
        if Ma[i][j]==1:
            Ma[i][j]=0
            cnt+=1
            search(i,j)
            result+=[cnt]
            cnt_+=1
            cnt=0
print(cnt_)
for i in range(len(result)-1,0,-1):
    for k in range(0,i):
        if result[k]>result[k+1]:
            result[k],result[k+1]=result[k+1],result[k]
for i in result:
    print(i)