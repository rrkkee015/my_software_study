import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())
for i in range(testcases):
    N=int(input())
    tree=[[0,0,0] for i in range(N+1)]
    