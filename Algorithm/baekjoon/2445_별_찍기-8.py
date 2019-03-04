N=int(input())
for _ in range(1,N+1):
    result='*'*_+' '*(2*N-2*_)+'*'*_
    print(result)
for __ in range(N-1,0,-1):
    result='*'*__+' '*(2*N-2*__)+'*'*__
    print(result)