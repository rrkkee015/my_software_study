#  class Node:
#     def __init__(self,item):
#         self.item=item
#         self.next=None
#
# def eQ(item):
#     global front, end
#     newnode=Node(item)
#     if front==None:
#         front=newnode
#     else:
#         end.next=newnode
#     end=newnode
#
# def dQ():
#     global front, end
#     if front==None:
#         return 'empty'
#     item=front.item
#     front=front.next
#     if front==None:
#         end=None
#     return item
#
# def search(i):
#     print(i,end=' ')
#     for j in range(N+1):
#         if mat[i][j] == 1 and visited[j]==False:
#             visited[j]=True
#             search(j)
#
#
# N,M,V=list(map(int,input().split()))
# mat=[[0]*(N+1) for i in range(N+1)]
# visited=[False]*(N+1)
# front=None
# end=None
# for i in range(M):
#     s,g=list(map(int,input().split()))
#     mat[s][g]=1
#     mat[g][s]=1
# visited[V]=True
# search(V)
# print()
# visited=[False]*(N+1)
# eQ(V)
# visited[V]=True
# while True:
#     take=dQ()
#     if take=='empty':
#         break
#     print(take, end=' ')
#     for i in range(N+1):
#         if mat[take][i] == 1 and visited[i]==False:
#             eQ(i)
#             visited[i]=True

N, M, V = map(int,input().split())
mat = [[] for _ in range(N + 1)]

for _ in range(M):
    s, g = map(int,input().split())
    mat[s].append(g)
    mat[g].append(s)

for _ in range(len(mat)):
    if mat[_]:
        mat[_] = sorted(mat[_])

visited = [1 for _ in range(N + 1)]
dfs_result = []
def dfs(go):
    dfs_result.append(str(go))
    for _ in mat[go]:
        if visited[_]:
            visited[_] = 0
            dfs(_)
visited[V] = 0
dfs(V)
print(' '.join(dfs_result))

import collections
dq = collections.deque()
visited = [1 for _ in range(N + 1)]
visited[V] = 0
dq.append(V)
bfs_result = []
while dq:
    v = dq.popleft()
    bfs_result.append(str(v))
    for _ in mat[v]:
        if visited[_]:
            visited[_] = 0
            dq.append(_)
print(' '.join(bfs_result))







