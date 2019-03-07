import sys
sys.stdin=open('sample_input.txt','r')

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

testcases=int(input())
for tc in range(testcases):
    N = int(input())
    maze = [[0] * N for _ in range(N)]
    dxdy = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    result = 0
    front,end=(None,None)
    for i in range(N):
        x = input()
        for j in range(N):
            maze[i][j] = int(x[j])
            if maze[i][j] == 2:
                S = [i, j]
            if maze[i][j] == 3:
                G = [i, j]
    eQ(S)
    while front!=None:
        temp=dQ()
        for _ in dxdy:
            if 0 <= _[0] + temp[0] < N and 0 <= _[1] + temp[1] < N and maze[_[0] + temp[0]][_[1] + temp[1]] == 3:
                result=1
            if 0<=_[0]+temp[0]<N and 0<=_[1]+temp[1]<N and maze[_[0]+temp[0]][_[1]+temp[1]]==0:
                y=_[0]+temp[0]
                x=_[1]+temp[1]
                maze[y][x]=1
                eQ([y,x])
        for i in maze:
            print(i)
        print()
    print(f'{tc+1} {result}')