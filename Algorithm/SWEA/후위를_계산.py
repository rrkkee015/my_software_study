inp='234*5/+'
inp='6528-*2/+'
inp='326+2/43*-+5+67*-'
stack=[0]*100
top=-1
for i in inp:
    if '0'<=i<='9':
        top+=1
        stack[top]=int(i)
    elif i=='+':
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
print(stack[0])