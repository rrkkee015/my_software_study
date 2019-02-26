import sys
sys.stdin=open('sample_input.txt','r')

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

def find2(lis):
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if lis[i][j]==2:
                x,y=j,i
    return x,y

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    front=None
    end=None
    cnt=0
    dxdy=[(1,0),(0,1),(-1,0),(0,-1)]
    maze_=[[int(i) for i in input()] for j in range(N)]
    x,y=find2(maze_)
    eQ([y, x,0])
    out=True
    while out:
        take=dQ()
        y=take[0]
        x=take[1]
        cnt=take[2]
        if take=='empty' :
            cnt=0
            break
        for i in dxdy:
            if 0<=y+i[0]<=N-1 and 0<=x+i[1]<=N-1 and maze_[y+i[0]][x+i[1]] == 3:
                out=False
                cnt=take[2]
                break
            elif 0<=y+i[0]<=N-1 and 0<=x+i[1]<=N-1 and maze_[y+i[0]][x+i[1]]==0:
                eQ([y + i[0],x + i[1],cnt+1])
                maze_[y + i[0]][x + i[1]]=1
    print(f'#{tc+1} {cnt}')