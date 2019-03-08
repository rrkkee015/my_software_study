class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def eQ(item):
    global front, end
    newnode=Node(item)
    if front==None:
        front=newnode
    else:
        end.next=newnode
    end=newnode

def dQ():
    global front, end
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end=None
    return item

N=int(input())
mat=[[0]*N for _ in range(N)]
max_rain=0
front=None
end=None
dxdy=[(0,1),(1,0),(-1,0),(0,-1)]
result=0
for i in range(N):
    lis=list(map(int,input().split()))
    if max_rain<max(lis):
        max_rain=max(lis)
    for j in range(N):
        mat[i][j]=[lis[j],0]

for rain in range(0,max_rain+1):
    cnt=0
    for i in range(N):
        for j in range(N):
            if mat[i][j][0] > rain:
                mat[i][j][1]=1
    for i in range(N):
        for j in range(N):
            if mat[i][j][1]==1:
                cnt+=1
                eQ([i,j])
                mat[i][j][1]=3
                while front != None:
                    temp=dQ()
                    y=temp[0]
                    x=temp[1]
                    for _ in dxdy:
                        if 0<=y+_[0]<N and 0<=x+_[1]<N and mat[y+_[0]][x+_[1]][1]==1:
                            eQ([y+_[0],x+_[1]])
                            mat[y+_[0]][x+_[1]][1]=3
    for i in range(N):
        for j in range(N):
            mat[i][j][1]=0

    if result<cnt:
        result=cnt

print(result)