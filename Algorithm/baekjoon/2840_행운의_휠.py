class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
        self.prev=None

def eQ(item):
    global front, end
    newnode=Node(item)
    if front==None:
        front=newnode
    else:
        end.next=newnode
        newnode.prev=end
    end=newnode

def dQ():
    global front, end
    if front==None:
        return 'empty'
    item=front.item
    front=front.prev
    if front==None:
        end=None
    return item

def link():
    global front, end
    front.prev=end
    end.next=front

def go():
    global front, end
    front=front.next

def insert(item):
    global front, end, result
    if front.item=='?' or front.item==item:
        front.item=item
    else:
        result='!'

N,K=tuple(map(int,input().split()))
front,end=(None,None)
result=''
for _ in range(N):
    eQ('?')

link()

for _ in range(K):
    S,W=list(map(str,input().split()))
    S=int(S)
    for k in range(S):
        go()
    insert(W)
    if result=='!':
        break

if result == '!':
    print(result)
else:
    start=front
    result+=dQ()
    while front != start:
        temp=dQ()
        if temp in result and temp != '?':
            result='!'
            break
        else:
            result+=temp
    if result=='!':
        print(result)
    else:
        print(result)