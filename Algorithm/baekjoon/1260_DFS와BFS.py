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

def search(i):
    print(i,end=' ')
    for j in range(N+1):
        if mat[i][j] == 1 and visited[j]==False:
            visited[j]=True
            search(j)


N,M,V=list(map(int,input().split()))
mat=[[0]*(N+1) for i in range(N+1)]
visited=[False]*(N+1)
front=None
end=None
for i in range(M):
    s,g=list(map(int,input().split()))
    mat[s][g]=1
    mat[g][s]=1
visited[V]=True
search(V)
print()
visited=[False]*(N+1)
eQ(V)
visited[V]=True
while True:
    take=dQ()
    if take=='empty':
        break
    print(take, end=' ')
    for i in range(N+1):
        if mat[take][i] == 1 and visited[i]==False:
            eQ(i)
            visited[i]=True