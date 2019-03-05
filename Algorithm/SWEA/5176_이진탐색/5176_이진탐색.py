import sys
sys.stdin=open('sample_input.txt','r')

def inorder(T):
    global cnt
    if T<=N:
        inorder(T*2)
        tree[T]=cnt
        cnt+=1
        inorder(T*2+1)

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    cnt=1
    tree=[0]*(N+1)
    inorder(1)
    print('#{} {} {}'.format(tc+1, tree[1],tree[N//2]))
