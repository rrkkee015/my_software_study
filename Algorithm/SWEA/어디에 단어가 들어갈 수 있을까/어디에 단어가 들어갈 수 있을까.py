import sys
sys.stdin=open('input.txt','r')

testcases=int(input())

for tc in range(testcases):
    N,K=list(map(int,input().split()))
    mat=[list(map(int,input().split())) for _ in range(N)]
    result=[]
    for i in range(N):
        cnt=0
        for j in range(N):
            if mat[i][j]==1:
                cnt+=1
            elif mat[i][j]==0:
                result+=[cnt]
                cnt=0
        else:
            result+=[cnt]
            cnt=0
    for j in range(N):
        cnt=0
        for i in range(N):
            if mat[i][j]==1:
                cnt+=1
            elif mat[i][j]==0:
                result+=[cnt]
                cnt=0
        else:
            result+=[cnt]
            cnt=0
    cnt=0
    for _ in result:
        if _ == K:
            cnt+=1
    print('#{} {}'.format(tc+1,cnt))