import sys
sys.stdin=open('sample_input.txt','r')

class Node:
    def __init__(self,item):
        self.prev=None
        self.next=None
        self.item=item

def eQ(item):
    global front, end
    newnode=Node(item)
    if front==None:
        front=newnode
    else:
        end.next=newnode
        newnode.prev=end
    end=newnode

def insert(item):
    global front, end
    insertnode=Node(item)
    p=front
    while p.item<=insertnode.item[0]:
        if p.next==None:
            break
        else:
            p=p.next
    temp=p.item
    for _ in range(len(item)):
        newnode=Node(item[_])
        if p.prev==None:
            newnode.next=p
            p.prev=newnode
            front=front.prev
        elif p.next==None and temp<item[0]:
            newnode.prev=p
            p.next=newnode
            end=end.next
            p=p.next
        else:
            newnode.next=p
            newnode.prev=p.prev
            p.prev.next=newnode
            p.prev=newnode

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
    N,M=tuple(map(int,input().split()))
    for __ in range(M):
        if __==0:
            lis=list(map(int,input().split()))
            for ___ in lis:
                eQ(___)
        else:
            lis=list(map(int,input().split()))
            insert(lis)
    print(f'#{tc + 1}', end=' ')
    for _ in range(10):
        print(f'{dQ()}', end=' ')
    print()
