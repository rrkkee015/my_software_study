class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def new(item):
    global front,end
    newnode=Node(item)
    if front==None:
        front=newnode
    else:
        end.next=newnode
    end=newnode

def insert(item):
    global front,end
    cnt=0
    newnode=Node(item)
    if line==0:
        newnode.next=front
        front=newnode
    else:
        p=front
        while p.next!=None:
            cnt+=1
            if line==cnt:
                newnode.next=p.next
                p.next=newnode
                return 1
            p=p.next
        p.next=newnode

def dQ():
    global front,end
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end=None
    return item

N=int(input())
lis=list(map(int,input().split()))
front,end=(None,None)
new(1)
result=[]
for i in range(2,N+1):
    line=lis[i-1]
    insert(i)
while front!=None:
    temp=dQ()
    result+=[temp]
for i in range(len(result)-1,-1,-1):
    print(result[i],end=' ')