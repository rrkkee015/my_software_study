import sys
sys.stdin=open('input.txt','r')
testcases=int(input())
for tc in range(testcases):
    N,M=list(map(int,input().split()))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    if len(A)>len(B):
        A,B=B,A
    le=abs(len(B)-len(A)+1)
    cnt=0
    result=-100
    while cnt!=le:
        temp=0
        for _ in range(len(A)):
            temp+=A[_]*B[cnt+_]
        if result<temp:
            result=temp
        cnt+=1
    print('#{} {}'.format(tc+1,result))