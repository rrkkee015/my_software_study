class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def eQ(item):
    global front, rear
    newNode=Node(item)
    if front==None:
        front=newNode
    else:
        rear.next=newNode
    rear=newNode

def dQ():
    global front, rear
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front ==None:
        rear=None
    return item

nums=20
idx=0
front=None
rear=None
while True:
    sn=[idx+1,0]
    eQ(sn)
    sn=dQ()
    nums-=sn[1]+1
    if nums<=0:
        print(sn[0])
        break
    else:
        taken=[sn[0],sn[1]+1]
        eQ(taken)
        idx+=1
