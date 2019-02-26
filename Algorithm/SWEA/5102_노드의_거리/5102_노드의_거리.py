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
    front=None
    end=None
    V,E=list(map(int,input().split()))
    mat=[[0]*(V+1) for i in range(V+1)]
    visited=[False]*(V+1)
    for i in range(E):
        a,b=list(map(int,input().split()))
        mat[a][b]=1
        mat[b][a]=1
    S,G=list(map(int,input().split()))
    eQ([S,0])
    visited[S]=True
    while True:
        take=dQ()
        cnt=take[1]
        if take[0]==G:
            print(f'#{tc+1} {take[1]}')
            break
        if take=='empty':
            print(f'#{tc+1} 0')
            break
        for i in range(len(mat)):
            if mat[take[0]][i] != 0 and visited[i]==False:
                eQ([i,cnt+1])
                visited[i]=True
            result=take

