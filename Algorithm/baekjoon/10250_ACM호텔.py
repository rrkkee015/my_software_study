testcases=int(input())
for tc in range(testcases):
    H,W,N=tuple(map(int,input().split()))
    cnt=0
    result=[[0 for i in range(H)] for j in range(W)]
    for i in range(1,W+1):
        for j in range(1,H+1):
            if i<10:
                result[i-1][j-1]=[str(j)+'0'+str(i)]
                cnt+=1
            elif i>=10:
                result[i-1][j-1]=[str(j)+str(i)]
                cnt+=1
            if cnt==N:
                print(int(result[i-1][j-1][0]))
