def Bubble(lis):
    for i in range(len(lis),0,-1):
        for j in range(0,i-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    nums=list(map(int,input().split()))
    Bubble(nums)
    result=nums[-1]-nums[0]
    print(f'#{tc+1} {result}')