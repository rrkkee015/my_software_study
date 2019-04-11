import itertools
N,M=map(int,input().split())
li=list(set(map(int,input().split())))
for _ in itertools.combinations_with_replacement(sorted(li),M):
    print(*_)