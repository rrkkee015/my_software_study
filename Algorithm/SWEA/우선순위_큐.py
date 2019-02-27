class Node:
    def __init__(self,item):
        self.item=item
        self.prev=None
        self.next=None

def eQ(item):
    global front, end
    newnode=Node(item)
    if front==None:
        front=newnode
        end=newnode
    elif front==end:
        end=newnode
        end.prev=front
        front.next=end
    else:
        p=end
        while p.item>newnode.item:
            p=p.prev
        newnode.next = p.next
        p.next.prev=newnode
        newnode.prev=p
        p.next = newnode


def dQ():
    global front, end
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end=None
    return item

lis=[1,5,4,2,3]
front,end=(None,None)
for i in lis:
    eQ(i)
while front !=None:
    print(dQ())