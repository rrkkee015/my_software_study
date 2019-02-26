class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def eq(item):
    global front, end
    newnode=Node(item)
    if front==None:
        front=newnode
    else:
        end.next=newnode
    end=newnode

def dq():
    global front, end
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end=None
    return item

front,end=(None,None)
N,M=list(map(int,input().split()))
maze=[[int(i) for i in input()] for k in range(N)]
eq([0,0,1])
maze[0][0]=0
dxdy=[(1,0),(0,-1),(-1,0),(0,1)]
out=True
while out:
    take=dq()
    y=take[0]
    x=take[1]
    cnt=take[2]
    if (y,x)==(N-1,M-1):
        result=cnt
        break
    for i in dxdy:
        if 0<=y+i[0]<N and 0<=x+i[1]<M and maze[y+i[0]][x+i[1]]==1:
            maze[y+i[0]][x+i[1]]=0
            a=y+i[0]
            b=x+i[1]
            eq([a,b,cnt+1])
print(result)