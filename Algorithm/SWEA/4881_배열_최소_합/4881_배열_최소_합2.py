import sys
sys.stdin=open('sample_input.txt','r')

def backtrack(c, top, sum):
    global min
    if top==N:
        if min>sum:
            min=sum
    elif sum>min:
        return 0
    else:
        for i in range(N):
            if i not in c:
                c.append(i)
                backtrack(c,top+1,sum+matrix[top][i])
                c.pop()
                print(c)

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    matrix=[list(map(int,input().split())) for i in range(N)]
    c=[]
    min=99999
    backtrack(c, 0, 0)
    print(f'#{tc+1} {min}')

# 1. DFS
# 2. 가지친다.