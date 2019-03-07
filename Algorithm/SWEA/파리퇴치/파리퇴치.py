import sys
sys.stdin=open('input.txt','r')

testcases=int(input())
for tc in range(testcases):
    N,M=list(map(int,input().split()))
    flys=[list(map(int,input().split())) for _ in range(N)]
    result=-1
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp=0
            for p in range(i,i+M):
                for q in range(j,j+M):
                    temp+=flys[p][q]
            if result<temp:
                result=temp
    print('#{} {}'.format(tc+1,result))