import sys
sys.stdin=open('sample_input.txt','r')

def soon(a, top,input,ssibal):
    global max_, lis_result, choiso
    if top == 0:
        ssibal=0
    c=[0]*max_
    result=''
    if top == input:
        for i in range(1, top+1):
            result+=str(a[i])
        the_sum = 0
        for i in range(len(result)):
            the_sum += matrix[i][int(result[i])-1]
        if choiso > the_sum:
            choiso= the_sum
        lis_result+=[result]
    else:
        top+=1
        nc=sibal(a,top,input,c)
        for i in range(nc):
            the_value = matrix[top-1][c[i]-1]
            if choiso>ssibal:
                a[top]=c[i]
                soon(a, top, input,ssibal +the_value)

def sibal(a, top,input,c):
    in_perm=[False]*10000
    for i in range(1, top):
        in_perm[a[i]]=True
    nc=0
    for i in range(1, input+1):
        if in_perm[i]==False:
            c[nc]=i
            nc+=1
    return nc

testcases=int(input())
for tc in range(testcases):
    lis_result=[]
    max_=1000
    N=int(input())
    matrix=[list(map(int,input().split())) for i in range(N)]
    top=0
    a=['-']*(N+1)
    choiso = 999999999
    soon(a,top,N,0)
    result=[]

    for k in lis_result:
        answer=0
        for i in range(N):
            answer+=matrix[i][int(k[i])-1]
        result+=[answer]
    print(f'#{tc+1} {min(result)}')