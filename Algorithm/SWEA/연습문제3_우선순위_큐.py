class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
        self.prev=None

def eQ(item):
    global Head, end
    newNode=Node(item)
    if Head==None:
        Head=newNode
        end=newNode
    elif Head==end:
        end=newNode
        Head.next=newNode
        end.prev=Head
    else:
        p=end
        while p.item>newNode.item:
            p=p.prev
        newNode.next=p.next
        p.next=newNode
        newNode.prev=p
        newNode.next.prev=newNode

def dQ():
    global Head, end
    if Head==None:
        return 'empty'
    item=Head.item
    Head=Head.next
    if Head==None:
        end=None
    return item

Head=None
end=None
lis=[1,5,2,4,3]
for i in lis:
    eQ(i)
while Head!=None:
    print(dQ())