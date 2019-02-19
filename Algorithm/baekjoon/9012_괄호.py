Testcases=int(input())
for tc in range(Testcases):
    sentence=input()
    stack=[0]*len(sentence)
    top=-1
    for j in range(len(sentence)):
        if sentence[j]=='(':
            top+=1
            stack[top]='('
        else:
            if top==-1:
                print('NO')
                break
            else:
                stack[top]=0
                top-=1
    else:
        if top==-1:
            print('YES')
        else:
            print('NO')