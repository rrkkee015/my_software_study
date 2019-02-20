inp='2+3*4/5'
inp='(6+5*(2-8)/2)'
inp='3+((2+6)/2-4*3)+5-6*7'
old='+-'
young='*/'

stack=[0]*100
top=-1

result=''

for i in inp:
    if top==-1 and i in '+-*/':
        top+=1
        stack[top]=i
    elif i == '(':
        top+=1
        stack[top]=i
    elif i == ')':
        while stack[top]!='(':
            result+=stack[top]
            top-=1
        stack[top]=0
        top-=1
    elif i in '+-*/':
        if i in young:
            if stack[top] in '*/':
                result+=stack[top]
                stack[top]=i
            else:
                top+=1
                stack[top]=i
        elif i in old:
            if stack[top] in '*/+-':
                result+=stack[top]
                stack[top]=i
            else:
                top+=1
                stack[top]=i
    else:
        result+=i
else:
    while top != -1:
        result+=stack[top]
        top-=1
print(result)