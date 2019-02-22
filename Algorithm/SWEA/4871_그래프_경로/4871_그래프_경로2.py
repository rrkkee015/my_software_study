import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

def solve(x):
    global state
    if x==G:
        state=True
        return 0
    else:
        if matrix[x][0] != 0:
            matrix[x][0] -= 1
            for k in range(1, len(matrix)):
                if k != 0:
                    sub=matrix[x][k]
                    matrix[x][k]=0
                    solve(sub)

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
    result = solve(S)
    if state==False:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} 1')