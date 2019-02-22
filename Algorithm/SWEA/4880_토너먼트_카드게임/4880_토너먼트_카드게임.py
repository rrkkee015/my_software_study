import sys
sys.stdin=open('sample_input.txt','r')

def winner(a,b):
    if a[0]-b[0]==1 or a[0]-b[0]==-2:
        return a
    elif a[0]-b[0]==-1 or a[0]-b[0]==2:
        return b
    else:
        return a

def partition(lis):
    if len(lis)==2:
        return winner(lis[0],lis[1])
    elif len(lis)==1:
        return lis[0]
    else:
        if len(lis)%2==1:
            pivot=len(lis)//2
        else:
            pivot=(len(lis)-1)//2
    a=partition(lis[0:pivot+1])
    b=partition(lis[pivot+1:len(lis)])
    return winner(a,b)

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    fake_lis=list(map(int,input().split()))
    lis=[[fake_lis[i],i+1] for i in range(N)]
    result=partition(lis)
    print(f'#{tc+1} {result[1]}')

