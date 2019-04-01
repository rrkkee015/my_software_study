def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    print(stack[top])
    top -= 1

stack = [0,0,0]
top = -1
push(5)
push(4)
push(3)
pop()
pop()
pop()