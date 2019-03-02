import sys
sys.stdin=open('sample_input.txt','r')

class Node:
    def __init__(self,item):
        self.item=item
        self.prev=None
        self.next=None

def eQ(item):
    global front, end
    newnode = Node(item)
    if front==None:
        front=newnode
    else:
        end.next=newnode
        newnode.prev=end
    end=newnode

def password():
    global front, end
    p=front
    for _ in range(K):
        for __ in range(1,M+1):
            if p==end and __ == M:
                newnode=Node(front.item+p.item)
                newnode.prev=p
                p.next=newnode
                p=newnode
                end=newnode
                break
            elif p==end and __ != M:
                p=front
            else:
                p=p.next
        else:
            newnode=Node(p.prev.item+p.item)
            newnode.prev=p.prev
            newnode.next=p
            p.prev.next=newnode
            p.prev=newnode
            p=newnode

def dQ():
    global front, end
    if end==None:
        return 'empty'
    item=end.item
    end=end.prev
    if end==None:
        front=None
    return item

testcases=int(input())

for tc in range(testcases):
    front=None
    end=None
    N,M,K=tuple(map(int,input().split()))
    N=list(map(int,input().split()))
    for _ in N:
        eQ(_)
    password()
    print(f'#{tc+1}', end=' ')
    for __ in range(10):
        result=dQ()
        if result=='empty':
            break
        else:
            print(f'{result}', end=' ')
    print()