def DFS(a,b):
    global time
    for _ in dxdy:
        if 0<=a+_[0]<y-1 and 0<=b+_[1]<x-1 and cheeze[a+_[0]][b+_[1]]==0:
            cheeze[a][b]=2
            DFS(a+_[0],b+_[1])

def melt():
    global time
    for q in range(y):
        for w in range(x):
            if cheeze[q][w]==1:
                for _ in dxdy:
                    if 0<=q+_[0]<y-1 and 0<=w+_[1]<x-1 and cheeze[q+_[0]][w+_[1]]==2:
                        cheeze[q][w]=0

y,x=list(map(int,input().split()))
dxdy=[(0,1),(0,-1),(1,0),(-1,0)]
time=0
cheeze=[list(map(int,input().split())) for i in range(y)]
for i in range(y):
    for j in range(x):
        if cheeze[i][j]==0:
            cheeze[i][j]=2
            DFS(i,j)
melt()
for i in cheeze:
    print(i)