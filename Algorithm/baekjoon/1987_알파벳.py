def move(i,j,cnt):
    global result,y,x
    for _ in dxdy:
        if 0<=_[0]+i<y and 0<=_[1]+j<x and visited[ord(mat[_[0]+i][_[1]+j])-65]==False:
            ni=_[0]+i
            nj=_[1]+j
            cnt+=1
            visited[ord(mat[ni][nj])-65]=True
            move(ni,nj,cnt)
            visited[ord(mat[ni][nj])-65]=False
            cnt-=1
        else:
            if result<cnt:
                result=cnt

y,x=list(map(int,input().split()))
dxdy=[(0,1),(1,0),(-1,0),(0,-1)]
visited=[False for _ in range(26)]
mat=[]
result=0
for _ in range(y):
    mat.append(input())
visited[ord(mat[0][0])-65]=True
move(0,0,1)
print(result)