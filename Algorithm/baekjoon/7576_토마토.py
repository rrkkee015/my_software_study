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

w,h=list(map(int,input().split()))
mat=[list(map(int,input().split())) for _ in range(h)]
dxdy=[(0,1),(1,0),(-1,0),(0,-1)]
front,end=(None,None)
result=0

for i in range(h):
    for j in range(w):
        if mat[i][j]==1:
            eQ([i,j,0])

while front!=None:
    temp=dQ()
    y=temp[0]
    x=temp[1]
    cnt=temp[2]
    if result<cnt:
        result=cnt
    mat[y][x]=2
    for _ in dxdy:
        if 0<=y+_[0]<h and 0<=x+_[1]<w and mat[y+_[0]][x+_[1]]==0:
            eQ([y+_[0],x+_[1],cnt+1])
            mat[y+_[0]][x+_[1]]=2

for i in range(h):
    for j in range(w):
        if mat[i][j]==0:
            result=-1
print(result)