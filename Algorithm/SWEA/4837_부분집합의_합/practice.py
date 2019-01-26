import sys
sys.stdin=open('sample_input.txt','r')

def bi_search(li,N,K):
    n=len(li)
    real_result = 0
    for i in range(1<<n):
        result=0
        cnt=0
        for j in range(n):
            if i & (1<<j):
                result+=li[j]
                cnt+=1
        if result==K and cnt == N:
            real_result+=1
    return real_result

testcases=int(input())
for test in range(testcases):
    N,K = tuple(map(int,input().split()))
    real_result=bi_search([1,2,3,4,5,6,7,8,9,10,11,12],N,K)
    print(f'#{test+1} {real_result}')