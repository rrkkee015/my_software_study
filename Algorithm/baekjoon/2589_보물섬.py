class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def eQ(item):
    global front,end
    newnode=Node(item)
    if front==None:
        front=newnode
    else:
        end.next=newnode
    end=newnode

def dQ():
    global front,end
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end=None
    return item

# from collections import deque
# dq = deque()
# dq.append(item)
# dq.popleft()
# dq.pop()
# if dq: # if is not empty:

h,w=list(map(int,input().split()))
mat=[[0]*w for _ in range(h)]
front,end=(None,None)
dxdy=[(1,0),(0,1),(-1,0),(0,-1)]
result=0
for i in range(h):
    lis=input()
    for j in range(w):
        if lis[j]=='W':
            mat[i][j]=0
        else:
            mat[i][j]=1

for i in range(h):
    for j in range(w):
        if mat[i][j]==1:
            visited=[[-1]*w for _ in range(h)]
            eQ([i,j,0])
            visited[i][j]=0
            while front!=None:
                temp=dQ()
                y=temp[0]
                x=temp[1]
                le=temp[2]
                if result<le:
                    result=le
                for _ in dxdy:
                    if 0<=y+_[0]<h and 0<=x+_[1]<w and mat[y+_[0]][x+_[1]]==1 and visited[y+_[0]][x+_[1]]==-1:
                        eQ([y+_[0],x+_[1],le+1])
                        visited[y+_[0]][x+_[1]]=0
print(result)
