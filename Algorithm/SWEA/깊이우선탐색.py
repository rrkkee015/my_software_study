inp=[1,4,1,3,2,3,2,5,4,6]
mat=[[0 for i in range(10)] for j in range(10)]
for i in range(0,len(inp),2):
    mat[inp[i]][inp[i+1]]=1
    mat[inp[i+1]][inp[i]]=1
stack=[0 for i in range(10)]
visited=[False for k in range(10)]

top=-1
v=1
visited[1]=True
result='1'

while True:
    for i in range(len(mat[v])):
        if mat[v][i]==1 and visited[i]==False:
            top+=1
            visited[i] = True
            stack[top]=i
            v=i
            result+='-'+str(i)
            break
    else:
        # v=stack[top]
        # stack[top]=0
        # top-=1 #여기 틀림
        stack[top]=0
        top-=1
        v=stack[top]
    if top == -1:
        print(result)
        break
