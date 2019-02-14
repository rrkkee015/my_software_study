import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())
for tc in range(testcases):
    sentence=input()
    stack = [0 for i in range(len(sentence))]
    top=-1
    for i in sentence:
        top += 1
        stack[top] = i
        if top>=1:
            if stack[top]==stack[top-1]:
                stack[top]=0
                stack[top-1]=0
                top-=2
    cnt=0
    for i in stack:
        if i != 0:
            cnt+=1
    print(f'#{tc+1} {cnt}')