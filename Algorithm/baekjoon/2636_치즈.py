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

h,w=list(map(int,input().split()))
mat=[list(map(int,input().split())) for _ in range(h)]
done=[[0]*w for _ in range(h)]
dxdy=[(0,1),(1,0),(-1,0),(0,-1)]
front=None
end=None
cnt=0
result=0
while mat!=done:
    for i in range(h):
        for j in range(w):
            if mat[i][j]==0:
                cnt+=1
                eQ([i,j])
                mat[i][j]=2
                while front!=None:
                    temp=dQ()
                    y=temp[0]
                    x=temp[1]
                    for _ in dxdy:
                        if 0<=y+_[0]<h and 0<=x+_[1]<w and mat[y+_[0]][x+_[1]]==0:
                            eQ([y+_[0],x+_[1]])
                            mat[y+_[0]][x+_[1]]=2
                break
        if cnt!=0:
            break

    for i in range(h):
        for j in range(w):
            if mat[i][j]==1:
                eQ([i,j])
                while front!=None:
                    temp=dQ()
                    y=temp[0]
                    x=temp[1]
                    for _ in dxdy:
                        if 0 <=y+_[0]<h and 0<=x+_[1]<w and mat[y+_[0]][x+_[1]]==2:
                            mat[y][x]=3
                    if mat[y][x]==3:
                        for _ in dxdy:
                            if 0<=y+_[0]<h and 0<=x+_[1]<w and mat[y+_[0]][x+_[1]]==1:
                                eQ([y+_[0],x+_[1]])
    cheeze = 0
    for i in range(h):
        for j in range(w):
            if mat[i][j]==3:
                cheeze+=1
            if mat[i][j]==3 or mat[i][j]==2:
                mat[i][j]=0
    result+=1
print(result)
print(cheeze)