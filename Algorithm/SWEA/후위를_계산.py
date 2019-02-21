inp='234*5/+'
inp='6528-*2/+'
inp='952*1++33*7*6*9*1*7*1+86*61*1*5*2*++4*7*43*8*2*6*78*4*5*+3+7+26+5+1+7+6+73*62+*6+6++2*4+22*49*3*+++++'
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