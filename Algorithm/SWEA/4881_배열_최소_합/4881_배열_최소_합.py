import sys
sys.stdin=open('sample_input.txt','r')

def min_sum(stack,top, sum):
    global min
    if top == N-1:
        if min > sum:
            min=sum
    elif min<sum:
        return 0
    else:
        for i in range(N):
            if i not in stack:
                top+=1
                stack[top]=i
                sum += matrix[top][i]
                min_sum(stack, top, sum)
                sum -= matrix[top][i]
                stack[top]='-'
                top-=1

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    matrix=[list(map(int,input().split())) for i in range(N)]
    top=-1
    stack=['-']*N
    min=1000000
    min_sum(stack,top, 0)
    print(f'#{tc+1} {min}')