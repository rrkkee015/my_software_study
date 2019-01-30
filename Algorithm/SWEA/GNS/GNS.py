import sys
sys.stdin=open('GNS_test_input.txt','r')
testcases=int(input()) # 10번의 테스트 케이스를 받는다.
for test in range(testcases): # 테스트 케이스 10번 돌린다.
    testcase, testnum = tuple(input().split())
    GNS=input().split()
    nums = {'ZRO ':0,'ONE ':0,'TWO ':0,'THR ':0,'FOR ':0,'FIV ':0,'SIX ':0,'SVN ':0,'EGT ':0,'NIN ':0} # 각자 ZRO
    result = ''
    for  i in GNS:
        nums[i +' ']+=1
    for k in nums:
        result += k*nums[k]
    print(f'{testcase}\n{result}')