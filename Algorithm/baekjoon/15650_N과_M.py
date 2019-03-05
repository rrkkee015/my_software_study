N,M=list(map(int,input().split()))
fake=[0]*N
result=[]
for _ in range(1,N+1):
    fake[_-1]=_
for i in range(1<<N):
    temp=[]
    for j in range(N):
        if i & 1<<j:
            temp+=[fake[j]]
    result+=[temp]
for _ in sorted(result):
    if len(_)==M:
        for i in _:
            print(i, end=' ')
        print()