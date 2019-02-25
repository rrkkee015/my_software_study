import sys
sys.stdin=open('sample_input.txt','r')
class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def eq(item):
    global front, end
    newnode=Node(item)
    if front==None:
        front=newnode
    else:
        end.next=newnode
    end=newnode

def dq():
    global front, end
    if front == None:
        return 'empty'
    item=front.item
    front=front.next
    if front==None:
        end=None
    return item

testcases=int(input())
for tc in range(testcases):
    front=None
    end=None
    N,M=tuple(map(int,input().split()))
    N=list(map(int,input().split()))
    for i in N:
        eq(i)
    for i in range(M):
        take=dq()
        eq(take)
    print(f'#{tc+1} {dq()}')
    while front !=None:
        dq()













# import sys
# sys.stdin=open('sample_input.txt','r')
#
# class Node:
#     def __init__(self,item):
#         self.item=item
#         self.next=None
#
# def eq(item):
#     global front, end
#     newnode=Node(item)
#     if front == None:
#         front = newnode
#     else:
#         end.next = newnode
#     end = newnode
#
# def dq():
#     global front, end
#     if front == None:
#         return 'empty'
#     item=front.item
#     front=front.next
#     if front == None:
#         end=None
#     return item
#
# testcases=int(input())
# front=None
# end=None
# for tc in range(testcases):
#     N,M=list(map(int,input().split()))
#     N=list(map(int,input().split()))
#     for i in range(len(N)):
#         eq(N[i])
#     for k in range(M):
#         take=dq()
#         eq(take)
#     print(f'#{tc+1} {dq()}')
#     while front != None:
#         dq()
