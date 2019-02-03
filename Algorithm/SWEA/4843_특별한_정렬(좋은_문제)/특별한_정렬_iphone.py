import sys
sys.stdin=open('sample_input.txt','r')

testcases=int(input())
for tc in range(testcases):
    N = int(input())
    lis = list(map(int,input().split()))
    result = ''
    for i in range(len(lis)):
        if i % 2 == 0:
            max_ = i
            for j in range(i+1,len(lis)):
                if lis[max_]<lis[j]:
                    max_=j
            lis[i],lis[max_]=lis[max_],lis[i]
        else:
            min_=i
            for j in range(i+1,len(lis)):
                if lis[min_]>lis[j]:
                    min_=j
            lis[i],lis[min_]=lis[min_],lis[i]
    for k in lis[:10]:
        result += str(k) + ' '
    print(f'#{tc+1} {result}')