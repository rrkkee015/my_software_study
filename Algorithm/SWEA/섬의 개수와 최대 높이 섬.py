class Node: #BFS 사용
    def __init__(self,item):
        self.item=item
        self.next=None

def eQ(item): #큐 삽입
    global front, end
    newnode=Node(item)
    if front==None:
        front=newnode
    else:
        end.next=newnode
    end=newnode

def dQ(): #큐 빼기
    global front, end
    if front==None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end=None
    return item

testcases = int(input())
for tc in range(testcases):
    front=None
    end=None
    N=int(input())
    mat=[list(map(int,input().split())) for _ in range(N)]
    dxdy=[(0,1),(1,0),(-1,0),(0,-1)]
    result=-1
    cnt=0
    for i in range(N):
        for j in range(N):
            if mat[i][j]!=0:
                eQ([i,j,mat[i][j]])
                mat[i][j]=0
                while front!=None:
                    temp=dQ()
                    y=temp[0]
                    x=temp[1]
                    h=temp[2]
                    if result<h:
                        result=h
                    for _ in dxdy:
                        if 0<=y+_[0]<N and 0<=x+_[1]<N and mat[y+_[0]][x+_[1]] != 0:
                            eQ([y+_[0],x+_[1],mat[y+_[0]][x+_[1]]])
                            mat[y+_[0]][x+_[1]]=0
                cnt+=1
    print('#{} {} {}'.format(tc+1,cnt,result))