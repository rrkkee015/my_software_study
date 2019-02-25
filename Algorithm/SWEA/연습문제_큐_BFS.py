class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def eQ(item):
    global front,end
    newnode=Node(item)
    if front == None:
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
        end=None
    return item

front=None
end=None
mat=[[0]*8 for i in range(8)]
visited=[False]*8
inp=[1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
for i in range(0,len(inp),2):
    mat[inp[i]][0]+=1
    mat[inp[i]][mat[inp[i]][0]]=inp[i+1]
visited[1]=True
eQ(1)
for i in range(len(mat)):
    if mat[i][0]!=0:
        for k in range(1,len(mat)):
            if mat[i][k] != 0 and visited[mat[i][k]]==False:
                eQ(mat[i][k])
                visited[mat[i][k]]=True

while front != None:
    print(dQ(), end='')





# class Node:
#     def __init__(self,item):
#         self.item=item
#         self.next=None
#
# def eQ(item):
#     global front, rear
#     newNode=Node(item)
#     if front == None:
#         front=newNode
#     else:
#         rear.next=newNode
#     rear=newNode
#
# def dQ():
#     global front, rear
#     if front==None:
#         return 'empty'
#     item=front.item
#     front=front.next
#     if front == None:
#         rear=None
#     return item
#
# inp=[1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# front=None
# rear=None
# path=[[0]*8 for i in range(8)]
# visited=[False]*8
# for i in range(0, len(inp), 2):
#     path[inp[i]][0]+=1
#     path[inp[i]][path[inp[i]][0]]=inp[i+1]
# eQ(1)
# visited[1]=True
# result=[]
# while True:
#     t=dQ()
#     result+=[t]
#     for i in path[t]:
#         if i != 0 and visited[i] == False:
#             visited[i]=True
#             eQ(i)
#     if False in visited[1:]:
#         continue
#     else:
#         while front != None:
#             result+=[dQ()]
#         break
# print(result)
#
#
