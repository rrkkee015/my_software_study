import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())
for tc in range(testcases):
    N,M,L= list(map(int,input().split()))
    tree=[0]*(N+2)
    for _ in range(M):
        A,B=tuple(map(int,input().split()))
        tree[A]=B
    for _ in range(len(tree)-2,0,-1):
        if tree[_]==0:
            tree[_]=tree[_*2]+tree[_*2+1]
    print('#{} {}'.format(tc+1,tree[L]))