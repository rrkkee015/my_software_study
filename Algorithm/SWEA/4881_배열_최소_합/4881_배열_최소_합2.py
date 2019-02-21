import sys
sys.stdin=open('sample_input.txt','r')
def backtrack(a, k ,input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        for i in range(1, k):
            print(a[i], end=" ")
        print()
    else:
        k+=1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    in_perm=[False] * MAX

    for i in range(1,k):
        in_perm[a[i]] = True

        ncandidates = 0
        for i in range(0, input):
            if in_perm[i] ==False:
                c[ncandidates]=i
                ncandidates+=1
        return ncandidates

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    MAXCANDIDATES=N
    MAX=N
    matrix=[list(map(int,input().split())) for i in range(N)]
    k=0
    a=[0]*(N+1)
    choiso = 999999999
    backtrack(a,k,N)