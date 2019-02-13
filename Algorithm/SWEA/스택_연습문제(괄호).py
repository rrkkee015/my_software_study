inp='()()((()))'
inp='((()))())'
stack=[0 for i in range(50)]
top=-1
for i in range(len(inp)):
    if inp[i] == '(':
        top+=1
        stack[top]=inp[i]
    else:
        stack[top]=0
        top-=1
        if top <-1:
            print('error')
            break
else:
    if stack==[0 for i in range(50)]:
        print('good')
    else:
        print('error')