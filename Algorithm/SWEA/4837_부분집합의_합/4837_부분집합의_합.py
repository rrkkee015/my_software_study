import sys

sys.stdin=open('sample_input.txt','r')

testcases=int(input())
for testcase in range(testcases):
    N,K = tuple(map(int,input().split()))

    lis = [1,2,3,4,5,6,7,8,9,10,11,12]

    n = len(lis)

    lis_null = [0]*n

    real_cnt = 0
    def my_sum(lis):
        result = 0
        for num in lis:
            result += num
        return result

    def my_count(lis):
        cnt = 0
        for i in lis:
            if i !=0:
                cnt += 1
        return cnt

    for i in range(1 << n):
        for k in range(n):
            if i & (1 << k):
                lis_null[k]=lis[k]
        if my_sum(lis_null) == K and  my_count(lis_null) == N:
            real_cnt += 1
        lis_null=[0]*n
    print(f'#{testcase+1} {real_cnt}')