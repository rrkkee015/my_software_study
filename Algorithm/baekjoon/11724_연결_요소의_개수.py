import sys
sys.setrecursionlimit(10**9)
# def find(i):
#     visited[i]=False
#     for _ in range(len(mat[i])):
#         if visited[mat[i][_]]:
#             find(mat[i][_])

def dfs(i):
    if visited[i]:
        visited[i]=False
        for _ in mat[i]:
            dfs(_)

N,M = list(map(int,input().split()))
mat=[[] for _ in range(N+1)]
for _ in range(M):
    S,G = list(map(int,input().split()))
    mat[S].append(G)
    mat[G].append(S)
visited=[True]*(N+1)
cnt=0

for x in range(1,len(mat)):
    if visited[x]:
        cnt+=1
        dfs(x)
print(cnt)