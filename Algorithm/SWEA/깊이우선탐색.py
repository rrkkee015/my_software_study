inp=[1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
matrix=[[0 for i in range(7)] for j in range(7)]
for i in range(0, len(inp), 2):
    matrix[inp[i]-1][inp[i+1]-1]=1
    matrix[inp[i+1]-1][inp[i]-1]=1
#행렬을 만들었다.
stack=[0 for i in range(7)] #숫자가 7까지니까
visited=[False for i in range(7)]
#stack과 visited를 초기화 하였다.

def push(lis, i):
    global top
    top+=1
    lis[top]=1
    return lis

def my_pop(lis):
    global top
    if len(lis)=0:
        return 'error'
    else:
        result=lis[top]
        lis[top]=0
        top-=1
        return result

st=1
while True:
    for i in range(lis[st-1]):
        if lis[st-1][i]==1:
            stack = push(stack,i+1)
