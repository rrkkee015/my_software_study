def hack(s):
    global N,cnt
    for _ in range(len(mat[s])):
        if mat[s] and visited[mat[s][_]]==False:
            visited[mat[s][_]]=True
            cnt+=1
            hack(mat[s][_])

N,M=list(map(int,input().split()))
mat=[[] for _ in range(N+1)]
for _ in range(M):
    A,B=list(map(int,input().split()))
    mat[B].append(A)
    
s=1
temp=0
result=[0]*(N+1)
while s != N+1:
    cnt=0
    visited = [False] * (N + 1)
    visited[0] = True
    hack(s)
    result[s]=cnt
    s+=1
for _ in range(len(result)):
    if result[_]==max(result):
        print(_,end=' ')