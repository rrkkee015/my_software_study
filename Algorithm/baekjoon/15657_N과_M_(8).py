import itertools
N, M = map(int,input().split())
lis = sorted(list(map(int,input().split())))
for _ in itertools.combinations_with_replacement(lis,M):
    print(*_)