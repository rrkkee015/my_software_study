# import sys
# sys.stdin=open('input.txt','r')

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    s=N//2
    g=N//2
    result=0
    mat=[]
    for _ in range(N):
        temp=[]
        for __ in input():
            temp+=[int(__)]
        mat+=[temp]
    for i in range(N):

        for j in range(N):
            if s<=j<=g:
                result+=mat[i][j]
        if i<N//2:
            s-=1
            g+=1
        else:
            s+=1
            g-=1
    print('#{} {}'.format(tc+1,result))