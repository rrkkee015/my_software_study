from collections import deque

def bfs(_):
    visited = [False] * (N + 1)
    cnt = 0
    hacking = deque()
    hacking.append(_)
    visited[_] = True
    while hacking:
        temp = hacking.popleft()
        for __ in mat[temp]:
            if visited[__] == False:
                visited[__] = True
                hacking.append(__)
                cnt += 1
    return cnt


N, M = list(map(int,input().split()))

mat=[[] for _ in range(N+1)]
for _ in range(M):
    G,S=list(map(int,input().split()))
    mat[S].append(G)

result=deque()
result_num=0

for _ in range(1,N+1):
    cnt_=bfs(_)
    if result_num<cnt_:
        result_num=cnt_
        while result:
            result.pop()
        result.append(_)
    elif result_num==cnt_:
        result.append(_)
for _ in result:
    print(_,end=' ')