import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())

for tc in range(testcases):
    N=int(input())//10
    result=[0 for i in range(N+1)]
    result[0]=1
    result[1]=1
    for i in range(2, N+1):
        result[i]=2**(i-1)+result[i-2]
    print(f'#{tc+1} {result[-1]}')