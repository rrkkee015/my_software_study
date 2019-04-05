import sys
sys.stdin = open('sample_input.txt','r')

def permu(temp, used):
    if used == [0] * 4:
        result.append(temp)
        return
    for _ in range(len(used)):
        if _ == 0 and used[_] != 0:
            temp_used = used[:]
            temp_used[_] -= 1
            permu(temp + '+',temp_used)
        if _ == 1 and used[_] != 0:
            temp_used = used[:]
            temp_used[_] -= 1
            permu(temp + '-', temp_used)
        if _ == 2 and used[_] != 0:
            temp_used = used[:]
            temp_used[_] -= 1
            permu(temp + '*', temp_used)
        if _ == 3 and used[_] != 0:
            temp_used = used[:]
            temp_used[_] -= 1
            permu(temp + '/', temp_used)

testcases = int(input())
for tc in range(testcases):
    N = int(input())
    pm_cnt = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    result = []
    permu('',pm_cnt)
    max_ = -0xffffffffffffffffffff
    min_ = 0xffffffffffffffffffff
    for _ in result:
        temp_li = nums[:]
        for __ in range(len(_)):
            if _[__] == '+':
                temp_li[__ + 1] = temp_li[__] + temp_li[__ + 1]
            if _[__] == '-':
                temp_li[__ + 1] = temp_li[__] - temp_li[__ + 1]
            if _[__] == '/':
                if temp_li[__] < 0:
                    temp_li[__ + 1] = -(abs(temp_li[__]) // temp_li[__ + 1])
                else:
                    temp_li[__ + 1] = temp_li[__] // temp_li[__ + 1]
            if _[__] == '*':
                temp_li[__ + 1] = temp_li[__] * temp_li[__ + 1]
        if max_ < temp_li[-1]:
            max_ = temp_li[-1]
        if min_ > temp_li[-1]:
            min_ = temp_li[-1]
    print('#{} {}'.format(tc+1, max_-min_))