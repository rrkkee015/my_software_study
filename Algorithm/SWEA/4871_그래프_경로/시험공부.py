import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

def DFS(x):
    global result
    for _ in range(len(mat)):
        if mat[x][_]==1 and visited[_]==False:
            visited[_]=True
            if G==_:
                result=1
            else:
                DFS(_)
    else:
        return


for tc in range(testcases):
    N,M=list(map(int,input().split()))
    mat=[[0]*(N+1) for _ in range(N+1)]
    visited=[False]*(N+1)
    result=0
    for _ in range(M):
        s,g=list(map(int,input().split()))
        mat[s][g]=1
    S,G=list(map(int,input().split()))
    visited[S]=True
    DFS(S)
    print('#{} {}'.format(tc+1,result))