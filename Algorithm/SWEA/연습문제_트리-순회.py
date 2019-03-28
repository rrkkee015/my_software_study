#1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def preorder_traverse(T): #전위순회
    global result
    if T:
        result+=str(T)+' '
        preorder_traverse(history[T][0])
        preorder_traverse(history[T][1])

def inorder_traverse(T): #중위순회
    global result
    if T:
        inorder_traverse(history[T][0])
        result += str(T) + ' '
        inorder_traverse(history[T][1])

def postorder_traverse(T): #후위순회
    global result
    if T:
        postorder_traverse(history[T][0])
        postorder_traverse(history[T][1])
        result+=str(T)+' '

inp=list(map(int,input().split()))
max_=max(inp)
history=[[0,0,0] for i in range(max_+1)]
# edges = 12 # 간선
# history = [[0]*2 for _ in range(edges+2)]
result=''

for i in range(0,len(inp),2):
    P=inp[i]
    S=inp[i+1]
    if history[P][0]==0:
        history[P][0]=S
    elif history[P][0]!=0:
        history[P][1]=S
    history[S][2]=P

preorder_traverse(1)
print(result)
result=''
inorder_traverse(1)
print(result)
result=''
postorder_traverse(1)
print(result)