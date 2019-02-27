class Node:
    def __init__(self,item,next=None):
        self.item=item
        self.next=next

def push(i):
    global top
    top = Node(i, top)

def pop():
    global top
    if top==None: #빈 리스트이면 #큐의 디큐와 비슷
        print('error')
    else:
        data=top.data
        top=top.link #top이 가리키는 노드를 바꿨다.
        return data