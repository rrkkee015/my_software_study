import sys
sys.stdin=open('GNS_test_input.txt','r')
testcases=int(input())
for test in range(testcases):
    testcase, testnum = tuple(input().split())
    GNS=input().split()
    nums = ['ZRO ','ONE ','TWO ','THR ','FOR ','FIV ','SIX ','SVN ','EGT ','NIN ']
    cnt=[0]*10
    result=''
    for word in GNS:
        for k in range(0,len(nums)):
            if word+' ' == nums[k]:
                cnt[k]+=1
    for num in range(0,len(cnt)):
        result += cnt[num]*nums[num]
    print(f'{testcase}\n{result}')
