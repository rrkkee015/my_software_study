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

computers=int(input())
connect=int(input())
front=None
end=None
mat=[[0]*(computers+1) for _ in range(computers+1)]
visited=[False]*(computers+1)
cnt=0
for _ in range(connect):
    s,g=list(map(int,input().split()))
    mat[s][g]=1
    mat[g][s]=1
eQ(1)
visited[1]=True
while front!=None:
    temp=dQ()
    for _ in range(len(mat)):
        if visited[_]==False and mat[temp][_]==1:
            eQ(_)
            visited[_]=True
for _ in visited:
    if _ == True:
        cnt+=1
print(cnt-1)