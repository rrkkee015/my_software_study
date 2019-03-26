def dfs(x):
    global cnt
    cnt+=1
    for __ in range(len(mat_high[x])):
        if visited[mat_high[x][__]]:
            visited[mat_high[x][__]] = False
            dfs(mat_high[x][__])

def dfs_(x):
    global cnt
    cnt+=1
    for __ in range(len(mat_low[x])):
        if visited[mat_low[x][__]]:
            visited[mat_low[x][__]] = False
            dfs_(mat_low[x][__])

N, M = list(map(int,input().split()))

mat_high = [[] for _ in range(N+1)] # 키 큰 순
mat_low = [[] for _ in range(N+1)] # 키 작은 순
high = [0 for _ in range(N+1)]
low = [0 for _ in range(N+1)]

for _ in range(M):
    s,g = list(map(int,input().split()))
    mat_high[s].append(g)
    mat_low[g].append(s)

for _ in range(1, N+1):
    visited = [True] * (N+1)
    visited[_] = False
    cnt = 0
    dfs(_)
    high[_] = cnt

for _ in range(1, N+1):
    visited = [True] * (N+1)
    visited[_] = False
    cnt = 0
    dfs_(_)
    low[_] = cnt

cnt = 0
for _ in range(1, N+1):
    if high[_] + low[_] == N + 1:
        cnt+=1
print(cnt)