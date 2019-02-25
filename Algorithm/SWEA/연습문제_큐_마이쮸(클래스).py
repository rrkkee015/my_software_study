class Mai:
    def __init__(self,item):
        self.item=item
        self.next=None

def enQ(item):
    global front, rear
    newMai=Mai(item)
    if front == None:
        front= newMai
    else:
        rear.next=newMai
    rear=newMai

def deQ():
    global front, rear
    if front==None:
        print("empty")
        return None
    item=front.item
    front=front.next
    if front == None:
        rear=None
    return item

front=None
rear=None

nums=20
idx=1
# line=Mai(sn)
while True:
    sn = [idx, 1]
    enQ(sn)
    taken = deQ()
    print(taken)
    nums -= taken[1]
    if nums<=0:
        print(taken[0])
        break
    taken[1] += 1
    enQ(taken)
    idx+=1
