import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

for tc in range(testcases):
    sen=input()
    stack=[0 for i in range(100)]
    top=-1
    for i in range(len(sen)):
        if sen[i] == '(' or sen[i] =='{':
            top+=1
            stack[top]=sen[i]
        if sen[i] == '} ' or sen[i] == ')':
            if top == -1:
                print(f'#{tc + 1} 0')
                break
        if sen[i]==')':
            if stack[top]=='(':
                stack[top]=0
                top-=1
            else:
                print(f'#{tc + 1} 0')
                break
        if sen[i]=='}':
            if stack[top]=='{':
                stack[top]=0
                top-=1
            else:
                print(f'#{tc + 1} 0')
                break
    else:
        if top != -1: # stack != [0 for i in range(100)]
            print(f'#{tc+1} 0')
        else:
            print(f'#{tc+1} 1')