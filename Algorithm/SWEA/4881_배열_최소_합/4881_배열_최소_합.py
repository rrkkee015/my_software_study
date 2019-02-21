import sys
sys.stdin=open('sample_input.txt','r')

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    if k ==input:
        print(a)
    else:
        k+=1
        ncandidates=construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    c[0]=True
    c[1] = False
    return 2

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    matrix=[[list(map(int,input().split()))] for i in range(N)]
    MAXCANDIDATES = 11
    NMAX = 11
    a = [0] *NMAX
    backtrack(a, 0, N)