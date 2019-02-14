import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

for tc in range(testcases):
    V,E =tuple(map(int,input().split()))
    matrix=[[0 for i in range(V+1)] for i in range(V+1)]
    for line in range(E):
        i,j=tuple(map(int,input().split()))
        matrix[i][j]=1
    S,G=tuple(map(int,input().split()))
    stack = [0 for i in range(V)]
    stack[0]=S
    top=0
    visited=[False for i in range(V+1)]
    visited[S]=True
    v=S
    result=-1
    while result==-1:
        for j in range(len(matrix[v])):
            if stack[0] == S and stack[top] == G:
                result=1
                break
            if matrix[v][j]==1 and visited[j]==False:
                visited[j]=True
                top+=1
                stack[top]=j
                v=j
                break
        else:
            stack[top]=0
            top-=1
            v = stack[top]
        if top==-1:
            result=0
    print(f'#{tc+1} {result}')