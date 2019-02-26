import sys
sys.stdin=open('input.txt','r')

class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def eQ(item):
    global front, end
    newnode=Node(item) #큐에다가 새로운 값을 대입
    if front==None:
        front=newnode
    else:
        end.next=newnode #end가 과자뿌리면서 지나가는거
    end=newnode

def dQ():
    global front, end
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end=None
    return item

def my_max(lis):
    for i in range(len(lis)-1,0,-1):
        for j in range(0,i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis[-1]

testcases=10
for tc in range(10):
    tl,S=list(map(int,input().split()))
    path=list(map(int,input().split()))
    mat=[[0]*101 for i in range(101)]
    visited=[False]*101
    front=None
    end=None
    min=1000
    result_lis=[]
    for i in range(0, len(path), 2):
        mat[path[i]][path[i + 1]] = 1
    eQ([S,0])
    visited[S]=True
    max=0
    while True:
        take=dQ()
        cnt=take[1]
        if take=='empty':
            break
        if max < cnt:
            max = cnt
            result_lis = []
        if max== cnt:
            result_lis += [take[0]]
        for i in range(len(mat)):
            if mat[take[0]][i] !=0 and visited[i] == False:
                eQ([i,cnt+1])
                visited[i]=True
    print(f'#{tc+1} {my_max(result_lis)}')
