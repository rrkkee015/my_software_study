import sys
sys.stdin=open('sample_input.txt','r')

class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def eQ(item):
    global front, end
    newnode=Node(item)
    if front==None:
        front=newnode
    else:
        end.next=newnode
    end=newnode

def dQ():
    global front, end
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end==None
    return item

def prep(N): #화덕 준비
    global idx
    for i in range(N):
        eQ(M[idx])
        idx+=1

testcases=int(input())
for tc in range(testcases):
    N,M=list(map(int,input().split()))
    ch=list(map(int,input().split()))
    M=[[i+1,ch[i]] for i in range(len(ch))]
    front=None
    end=None
    idx=0
    prep(N)
    out=True
    while out:
        for _ in range(N):
            pizza=dQ()
            if pizza=='empty':
                out=False
                break
            if pizza[1]//2==0 and idx<len(M):
                eQ(M[idx])
                idx+=1
            elif pizza[1]//2!=0:
                eQ([pizza[0],pizza[1]//2])
            result=pizza[0]
    print(f'#{tc+1} {result}')