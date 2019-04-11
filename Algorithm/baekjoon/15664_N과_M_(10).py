import itertools

N, M = map(int,input().split())
li = sorted(list(map(int,input().split())))
result = []
for _ in itertools.combinations(li, M):
    result.append(_)
for _ in sorted(list(set(result))):
    print(*_)