import sys
sys.stdin=open('GNS_test_input.txt','r')
testcases=int(input())
for tc in range(testcases):
    testcase, cases = tuple(map(str,input().split()))
    numbers=input()
    numbers_list=[]
    cnt=0
    number = ''
    result=''
    for i in range(len(numbers)):
        if numbers[i]==' ':
            numbers_list+=[number]
            number=''
            continue
        else:
            number+=numbers[i]
    nums = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    cnt = [0 for i in range(10)]
    for i in range(len(numbers_list)):
        for j in range(len(nums)):
            if nums[j] in numbers_list[i]:
                cnt[j]+=1
                break
    for i in range(10):
        result += (nums[i]+' ')*cnt[i]
    print(f'{testcase}\n{result}')