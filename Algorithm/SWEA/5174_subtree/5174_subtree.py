import sys
sys.stdin=open('sample_input.txt','r')

def post(T):
    global cnt
    if T:
        post(tree[T][0])
        post(tree[T][1])
        cnt+=1

testcases=int(input())
for tc in range(testcases):
    cnt=0
    E,N=list(map(int,input().split()))
    lis=list(map(int,input().split()))
    tree=[[0,0,0] for _ in range(E+2)]
    for i in range(0, len(lis), 2):
        if tree[lis[i]][0]==0:
            tree[lis[i]][0]=lis[i+1]
        else:
            tree[lis[i]][1]=lis[i+1]
        tree[lis[i+1]][2]=lis[i]
    post(N)
    print('#{} {}'.format(tc+1,cnt))