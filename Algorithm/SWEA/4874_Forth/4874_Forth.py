import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

for tc in range(testcases):
    cal=list(map(str,input().split()))
    stack=[0]*len(cal)
    top=-1
    for i in cal[:-1]:
        if i=='+':
            stack[top-1]=stack[top-1]+stack[top]
            top-=1
        elif i=='-':
            stack[top-1]=stack[top-1]-stack[top]
            top-=1
        elif i=='*':
            stack[top-1]=stack[top-1]*stack[top]
            top-=1
        elif i=='/':
            stack[top-1]=stack[top-1]/stack[top]
            top-=1
        else:
            top+=1
            stack[top]=int(i)
    if top != 0:
        print(f'#{tc+1} error')
    else:
        print(f'#{tc+1} {int(stack[0])}')