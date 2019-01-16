import sys
sys.stdin=open('sample_input.txt','r')

T=int(input())
for j in range(1,T+1):
    N=int(input())
    L=list(map(int,input().split()))
    for i in range(len(L)-1,0,-1):
        for k in range(0,i):
            if L[k] > L[k+1]:
                L[k], L[k+1] = L[k+1], L[k]
        r=L[-1]-L[0]
    print(f'#{j} {r}')
        
