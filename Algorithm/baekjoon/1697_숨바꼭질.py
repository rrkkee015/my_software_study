from collections import deque

N, M = list(map(int,input().split()))
visited=[True]*200001
brother=deque()
p,cnt=N,0
brother.append([p,cnt])
min=10**9
if N > M :
    min=N-M
else:
    while brother:
        p, cnt = brother.popleft()
        if p == M:
            if min > cnt:
                min = cnt
            continue
        if p > M:
            if min > cnt + p - M:
                min = cnt + p - M
        else:
            if p*1<100001 and visited[p+1]:
                visited[p+1]=False
                brother.append([p+1,cnt+1])
            if p-1>=0 and visited[p-1]:
                visited[p-1]=False
                brother.append([p-1,cnt+1])
            if p*2<200000 and visited[p*2]:
                visited[p*2]=False
                brother.append([p*2,cnt+1])
print(min)