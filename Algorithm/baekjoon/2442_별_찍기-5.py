N=int(input())
for _ in range(1,N+1):
    result=' '*(N-_)+ '*'*(2*_-1)
    print(result)