class Node:
    def __init__(self,item,next=None):
        self.item=item
        self.next=next

class DoubleNode:
    def __init__(self,prev,item,next):
        self.prev=None
        self.item=item
        self.next=None

def addtoFirst(data):
    global Head
    Head = Node(data, Head)

def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link=Node(data, pre.link)

def addtoLast(data):
    global Head
    if Head==None:
        Head=Node(data,None)
    else:
        p=Head
        while p .link != None:
            p = p.link
        p.link = Node(data, None)

def delete(pre):
    if pre==None or pre.link==None:
        print('error')
    else:
        pre.link=pre.link.link





Head=None