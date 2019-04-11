def permu(li):
    if len(li) == M:
        print(*li)
    for _ in range(N):
        if visited[_]:
            visited[_] = 0
            li.append(lis[_])
            permu(li)
            li.pop()
            visited[_] = 1

N, M = map(int,input().split())
lis = sorted(list(map(int,input().split())))
visited = [1 for _ in range(N)]
permu([])

import itertools
N, M = list(map(int,input().split()))
lis = sorted(list(map(int,input().split())))
for _ in itertools.permutations(lis, M):
    print(*_)