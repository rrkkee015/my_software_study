def DFS(a,b):
    for _ in dxdy:
        if 0<=a+_[0]<y and 0<=b+_[1]<x and cheeze[a+_[0]][b+_[1]]==0:
            cheeze[a+_[0]][b+_[1]]=2
            DFS(a+_[0],b+_[1])

def melt():
    global time
    for i in range(y):
        for j in range(x):
            if cheeze[i][j]==1:
                for _ in dxdy:
                    if 0<=i+_[0]<y and 0<=j+_[1]<x and cheeze[i+_[0]][j+_[1]]==2:
                        cheeze[i][j]=0
    time+=1

y,x=list(map(int,input().split()))
dxdy=[(0,1),(-1,0),(1,0),(0,-1)]
time=0
result=False
cheeze=[list(map(int,input().split())) for i in range(y)]
DFS(0,0)
for i in cheeze:
    print(i)
print()
melt()
for i in cheeze:
    print(i)