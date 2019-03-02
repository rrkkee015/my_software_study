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

def I(item):
    global front, end
    newnode=Node(item)
    p=front
    ca=False
    while p.item[0] != item[0]:
        p=p.next
        if p.next==None:
            p.next=newnode
            newnode.prev=p
            ca=True
            break
    if ca==True:
        return 1
    newnode.next=p
    newnode.prev=p.prev
    if p.prev==None:
        p.prev=newnode
        front=front.prev
    else:
        p.prev.next=newnode
        p.prev=newnode
    while p.next != No ne:
        p.item[0]+=1
        p=p.next
    if p.next == None:
        p.item[0]+=1

def D(item):
    global front, end
    p=front
    while p.item[0] != item:
        p=p.next
    if p.prev==None and p.next==None:
        front=None
        end=None
    elif p.prev==None:
        front=front.next
        front.prev=None
        p.next=None
        p=front
        p.item[0]-=1
    elif p.next==None:
        end=end.prev
        end.next=None
        p.prev=None
        p=end
    else:
        p.prev.next=p.next
        p.next.prev=p.prev
        temp=p
        p=p.prev
        temp.next=None
        temp.prev=None
        temp=None
    while p.next != None:
        p=p.next
        p.item[0]-=1

def C(item):
    global front, end
    if end==None:
        return 1
    p=front
    while p.item[0] != item[0]:
        p=p.next
    p.item[1]=item[1]

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
    case=False
    N,M,L=tuple(map(int,input().split()))
    N=list(map(int,input().split()))
    for _ in range(len(N)):
        eQ([_,N[_]])
    for __ in range(M):
        quest=list(map(str,input().split()))
        for ___ in range(len(quest)):
            if ___ != 0:
                quest[___]=int(quest[___])
        if quest[0]=='I':
            quest=quest[1:]
            I(quest)
        elif quest[0]=='C':
            quest=quest[1:]
            C(quest)
        elif quest[0]=='D':
            D(quest[1])
    while front != None:
        result=dQ()
        if result[0]==L:
            result=result[1]
            case=True
            break
    if front==None and case==False:
        print(f'#{tc+1} -1')
    else:
        print(f'#{tc+1} {result}')