import sys
sys.stdin=open('sample_input.txt','r')

class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
        self.prev=None

def dQ():
    global front, end
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end = None
    return item

def eQ(item):
    global front, end
    newnode=Node(item)
    if front==None:
        front=newnode
    else:
        newnode.prev=end
        end.next=newnode
    end=newnode

def insert(item):
    global front, end
    insertnode=Node(item)
    p=end
    while p.item[1] != insertnode.item[1]:
        p=p.prev
    insertnode.next=p
    insertnode.prev=p.prev
    if p.prev != None:
        p.prev.next=insertnode
        p.prev=insertnode
    else:
        p.prev=insertnode
        front=front.prev
    s=end
    while s.item[1] != insertnode.item[1]:
        s.item[1]+=1
        s=s.prev
    s.item[1]+=1

testcases=int(input())
for tc in range(testcases):
    front=None
    end=None
    N,M,L=tuple(map(int,input().split()))
    N=list(map(int,input().split()))
    for i in range(len(N)):
        eQ([N[i],i])
    for _ in range(M):
        index,num=tuple(map(int,input().split()))
        insert([num,index])
    while front!=None:
        result=dQ()
        if result[1]==L:
            print(f'#{tc+1} {result[0]}')