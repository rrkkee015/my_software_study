import sys
sys.stdin=open('s_input.txt','r')

testcases=int(input())

def check(item):
    global result
    sitem=str(item)
    for _ in range(len(sitem)-1):
        if sitem[_]>sitem[_+1]:
            return
    else:
        if result<item:
            result=item

for tc in range(testcases):
    result=-1
    N=int(input())
    nums=list(map(int,input().split()))
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            temp=nums[i]*nums[j]
            check(temp)
    print(f'#{tc+1} {result}')