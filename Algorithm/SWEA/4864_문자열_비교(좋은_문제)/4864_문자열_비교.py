import sys
sys.stdin=open('sample_input.txt','r')
def BruteForce(a,b):
    i=0
    j=0
    M=len(a)
    N=len(b)
    while i<M and j<N:
        if a[i] != b[j]:
            j=j-i
            i=-1
        i=i+1
        j=j+1
    if i==M:
        return 1
    else:
        return 0
testcases=int(input())
for testcase in range(testcases):
    word=input()
    sentence=input()
    result=BruteForce(word,sentence)
    print(f'#{testcase+1} {result} ')