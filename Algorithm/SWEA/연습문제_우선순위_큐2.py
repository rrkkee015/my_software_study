class Node:
    def __init__(self, item):
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
        front.next=newnode
        end.prev=front
    else:
        p=end
        while newnode.item<p.item:
            p=p.prev
        newnode.prev=p
        newnode.next=p.next
        p.next.prev=newnode
        p.next=newnode

def dQ():
    global front, end
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end=None
    return item

front=None
end=None
lis=[1,5,2,4,3]
for i in lis:
    eQ(i)
while front!=None:
    print(dQ())
