import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

def solve(x,y):
    global state
    if x==y:
        state=True
        return 1
    else:
        if matrix[S][0] != 0:
            matrix[S][0] -= 1
            for k in range(1, len(matrix)):
                if k != 0:
                    solve(x,k)

for tc in range(testcases):
    V,E =tuple(map(int,input().split()))
    matrix=[[0 for i in range(V+1)] for i in range(V+1)]
    state=False
    for line in range(E):
        i,j=tuple(map(int,input().split()))
        matrix[i][0]+=1
        matrix[i][matrix[i][0]]=j
    S,G=tuple(map(int,input().split()))
    stack = [0 for i in range(V)]
    stack[0]=S
    top=0
    visited=[False for i in range(V+1)]
    visited[S]=True
    result = solve(S, G)
    if state==False:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} 1')