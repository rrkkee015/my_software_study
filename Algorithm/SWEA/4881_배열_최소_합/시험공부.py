import sys
sys.stdin=open('sample_input.txt','r')

def bt(visited,depth,temp):
    global min_
    if depth==N:
        if min_>temp:
            min_=temp
        return
    elif min_<temp:
        return
    else:
        for _ in range(N):
            if visited[_]==0:
                visited[_]=1
                bt(visited,depth+1,temp+mat[depth][_])
                visited[_]=0


testcases=int(input())
for tc in range(testcases):
    N=int(input())
    mat=[list(map(int,input().split())) for _ in range(N)]
    visited=[0]*N
    min_=71623762178461387
    bt(visited,0,0)
    print(min_)