import sys
sys.stdin=open('input.txt','r')

testcases=10

for tc in range(testcases):
    N=input()
    inp=input()
    stack = [0] * 10000
    top = -1
    post = ''
    for i in range(len(inp)):
        if inp[i] in '*/+-' and stack[0] == 0:
            top += 1
            stack[top] = inp[i]
        elif inp[i] == '(':
            top += 1
            stack[top] = inp[i]
        elif inp[i] == ')':
            while stack[top] != '(':
                post += stack[top]
                stack[top] = 0
                top -= 1
            stack[top] = 0
            top -= 1
        elif inp[i] == '*' or inp[i] == '/':
            if stack[top] == '/' or stack[top] == '*':
                post += stack[top]
                stack[top] = inp[i]
            else:
                top += 1
                stack[top] = inp[i]
        elif inp[i] == '+' or inp[i] == '-':
            if stack[top] == '(':
                top += 1
                stack[top] = inp[i]
            else:
                post += stack[top]
                stack[top] = inp[i]
        else:
            post += inp[i]
    while top != -1:
        post += stack[top]
        stack[top] = 0
        top -= 1
    for i in range(len(post)):
        if post[i]=='+':
            stack[top-1]=stack[top-1]+stack[top]
            top-=1
        elif post[i]=='-':
            stack[top-1]=stack[top-1]-stack[top]
            top-=1
        elif post[i]=='*':
            stack[top-1]=stack[top-1]*stack[top]
            top -= 1
        elif post[i]=='/':
            stack[top-1]=int(stack[top-1]/stack[top])
            top -= 1
        else:
            top+=1
            stack[top]=int(post[i])
    print(f'#{tc+1} {stack[0]}')