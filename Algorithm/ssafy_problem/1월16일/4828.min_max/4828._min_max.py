import sys
sys.stdin=open('sample_input.txt','r')

T=int(input())
for j in range(1,T+1):
    N=int(input())
    L=list(map(int,input().split()))
    for i in range(0,N):
        r=max(sorted(L))-min(sorted(L))
    print(f'#{j} {r}')
