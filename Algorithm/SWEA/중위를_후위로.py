# inp='(9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)*4*7+4*3*8*2*6+(7*8*4*5)+3+7+(2+6+5+1+7+6+7*3*(6+2)+6+6)*2+4+2*2+4*9*3)'
# inp='(6+5*(2-8)/2)'
inp='3+((2+6)/2-4*3)+5-6*7'
old='+-'
young='*/'

stack=[0]*100
top=-1

result=''

# for i in inp:
#     if top==-1 and i in '+-*/':
#         top+=1
#         stack[top]=i
#     elif i == '(':
#         top+=1
#         stack[top]=i
#     elif i == ')':
#         while stack[top]!='(':
#             result+=stack[top]
#             top-=1
#         stack[top]=0
#         top-=1
#     elif i in '+-*/':
#         if i in young:
#             if stack[top] in '*/':
#                 result+=stack[top]
#                 stack[top]=i
#             else:
#                 top+=1
#                 stack[top]=i
#         elif i in old:
#             if stack[top] in '*/+-':
#                 result+=stack[top]
#                 stack[top]=i
#             else:
#                 top+=1
#                 stack[top]=i
#     else:
#         result+=i
# else:
#     while top != -1:
#         result+=stack[top]
#         top-=1
# print(result)
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
            post +=stack[top]
            stack[top] = inp[i]
    else:
        post += inp[i]
while top !=-1:
    post+=stack[top]
    stack[top]=0
    top-=1
print(post)