import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    lis=[0]*(N+1)
    result=0
    temp=list(map(int,input().split()))
    for i in range(1,len(lis)):
        lis[i]=temp[i-1]
        par=i
        while par != 1:
            if lis[par//2]>lis[par]:
                lis[par//2],lis[par]=lis[par],lis[par//2]
            par=par//2
    while N!=1:
        N=N//2
        result+=lis[N]
    print('#{} {}'.format(tc+1,result))