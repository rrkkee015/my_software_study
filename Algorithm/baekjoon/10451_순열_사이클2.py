import sys
sys.setrecursionlimit(2000)

def solve(x):
    global cnt
    visited[x]=True
    if visited[lis[x-1]]==False:
        solve(lis[x-1])
    else:
        cnt+=1

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    lis=list(map(int,input().split()))
    visited=[False]*(N+1)
    visited[0]=True
    cnt=0
    for i in range(N+1):
        if visited[i]==False:
            solve(i)
    print(cnt)