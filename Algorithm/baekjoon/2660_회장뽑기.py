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
mat=[[0]*(N+1) for _ in range(N+1)]
front=None
end=None

while True:
    s,g=list(map(int,input().split()))
    if s==-1 and g==-1:
        break
    mat[s][g]=1
    mat[g][s]=1

scores=[0]*(N+1)
scores[0]=999999

for n in range(1,N+1):
    score=0
    visited = [False] * (N + 1)
    visited[0] = True
    eQ([n,0])
    visited[n]=True

    while front!=None:
        p=dQ()
        cnt=p[1]
        for _ in range(len(mat)):
            if mat[p[0]][_]==1 and visited[_]==False:
                visited[_]=True
                eQ([_,cnt+1])
        if score<p[1]:
            score=p[1]
    scores[n]=score
cn=0
result=''
for i in range(len(scores)):
    if scores[i]==min(scores):
        cn+=1
        result+=str(i)+' '
print(min(scores),end=' ')
print(cn)
print(result)