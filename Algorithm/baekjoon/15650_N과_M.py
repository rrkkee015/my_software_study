import itertools
N, M = map(int,input().split())
lis = [str(_ + 1) for _ in range(N)]
for _ in itertools.combinations(lis, M):
    print(' '.join(_))